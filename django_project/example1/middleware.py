from django.db import transaction
from django.http import JsonResponse
from rest_framework import status


class TransactionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Apply transaction only for write methods
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                with transaction.atomic():  # Start a transaction block
                    response = self.get_response(request)
                    if response.status_code >= 500:
                        transaction.set_rollback(True)
                        return response(f"API returned error with status code {response.status_code}")
            except Exception as e:
                # Ensure rollback happens and propagate the error
                 return JsonResponse(
                    {'message': 'Internal Server Error'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # For other HTTP methods, just process the request
            response = self.get_response(request)

        return response