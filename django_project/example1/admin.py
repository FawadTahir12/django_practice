# pylint: disable=missing-docstring
from django.contrib import admin
from .models import User, Author, Publisher,  Books

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['telephone', 'joindate']
class PublisherAdmin(admin.ModelAdmin):
    list_display = [ 'joindate']
class BooksAdmin(admin.ModelAdmin):
    list_display= ['title', 'genre', 'price']
admin.site.register(User, UserAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
