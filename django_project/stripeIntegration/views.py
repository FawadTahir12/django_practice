from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import stripe
from .models import StripeCustomer, PaymentHistory, Subscription
from django.utils import timezone

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_customer(request):
    try:
        # Create a customer in Stripe
        customer = stripe.Customer.create(
            email=request.user.email,
            metadata={
                'user_id': request.user.id
            }
        )
        
        # Save the customer in our database
        StripeCustomer.objects.create(
            user=request.user,
            stripe_customer_id=customer.id
        )
        
        return Response({
            'customer_id': customer.id,
            'message': 'Customer created successfully'
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_payment_intent(request):
    try:
        amount = request.data.get('amount')
        currency = request.data.get('currency', 'usd')
        
        # Get or create customer
        customer, _ = StripeCustomer.objects.get_or_create(user=request.user)
        
        # Create payment intent
        intent = stripe.PaymentIntent.create(
            amount=int(float(amount) * 100),  # Convert to cents
            currency=currency,
            customer=customer.stripe_customer_id,
            metadata={
                'user_id': request.user.id
            }
        )
        
        return Response({
            'client_secret': intent.client_secret
        })
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_POST
def webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        customer = StripeCustomer.objects.get(stripe_customer_id=payment_intent['customer'])
        
        PaymentHistory.objects.create(
            customer=customer,
            stripe_payment_intent_id=payment_intent['id'],
            amount=payment_intent['amount'] / 100,  # Convert from cents
            currency=payment_intent['currency'],
            status=payment_intent['status']
        )
    
    elif event['type'] == 'customer.subscription.created':
        subscription = event['data']['object']
        customer = StripeCustomer.objects.get(stripe_customer_id=subscription['customer'])
        
        Subscription.objects.create(
            customer=customer,
            stripe_subscription_id=subscription['id'],
            stripe_price_id=subscription['items']['data'][0]['price']['id'],
            status=subscription['status'],
            current_period_start=timezone.datetime.fromtimestamp(subscription['current_period_start']),
            current_period_end=timezone.datetime.fromtimestamp(subscription['current_period_end'])
        )
    
    return HttpResponse(status=200) 