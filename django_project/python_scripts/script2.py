
from copy import deepcopy, copy
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


class MYNumber:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MYNumber):
            return self.value == other.value
        return False

num1 = MYNumber(11111)
num2 = MYNumber(11111)
num3 = MYNumber(11111)
print(num1 == num3)
list1 = [[1,2,3], 1,2,3,[[299,MYNumber(29999),3]]]

list2 = deepcopy(list1)
# list2[2] = 10


print(list1)
print(list2)
print(list1[4][0][1] is list2[4][0][1])




class MyNum:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

a = MyNum(10)
b = MyNum(10)
print(a.__hash__())



# def myName(name):
#     return name

# print(myName.__call__("jim"))




def outer(func):
    an_name = "Fawad"
    def inner():
        hello = func()
        print(hello)
        return an_name
    return inner
    

# dd = outer("Jim")
# print(dd.__call__())

@outer
def hello():
    print("hello")
    return 1

print(hello())

print(globals())
print(locals())