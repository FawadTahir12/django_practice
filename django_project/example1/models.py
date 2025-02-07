from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import  AbstractUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone
from django_project.enums import USER_TYPE_CHOICES

class Author(models.Model):
    
    class Meta:
        db_table = "authors"
    
    address = models.CharField(max_length=200, null=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE, default=None, null=False, blank=False)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
    joindate = models.DateField(default=timezone.now)
    popularity_score = models.IntegerField(null=True)
    followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')

class Books(models.Model):
    
    class Meta:
        db_table = "books"
        
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')
    images = ArrayField(models.JSONField(),blank=True, default=None)
    def __str__(self):
        return self.title

class Publisher(models.Model):
    
    class Meta:
        db_table = "publishers"
    user = models.OneToOneField('User', models.CASCADE, null=False, blank=False, default=None)
    recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class User(AbstractUser, PermissionsMixin):
    
    class Meta:
        db_table = "users"   
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique = True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='Simple')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        
        if self.user_type == 'Author':
            Author.objects.get_or_create(user=self)
    def __str__(self):
        return self.email
    

