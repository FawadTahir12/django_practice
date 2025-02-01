

#  non primitive datatype
dict1 = {
    'name': 'test1',
}
dict2 = {
    'name': 'test1',
}
print(dict1 is dict2)
print(dict1 == dict2)

a= 10
b = 10
print(a is b)
print(a == b)


x = None
print(x == None)

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

# Apply the decorator
@logging_decorator
def add(a, b):
    return a + b

# Using the decorated function
print(add(3, 5))