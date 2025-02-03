from enum import StrEnum

class RequestEnum(StrEnum):
    POST = 'POST'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    PUT = 'PUT'
    GET = 'GET'
    
    
USER_TYPE_CHOICES = [
        ('Simple', 'Simple'),
        ('Author', 'Author'),
        ('Publisher', 'Publisher'),
    ]