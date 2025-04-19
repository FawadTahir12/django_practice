class Example:
    _instance = None  # Class variable to store the single instance
    count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.count += 1
            print(cls._instance, "instance")
            print(f"Creating first instance. Count: {cls.count}")
            return cls._instance
        else:
            print("Error: Cannot create more than one instance of this class")
            return cls._instance

    def __init__(self, data):
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        if not hasattr(self, 'initialized'):
            
            self.data = data
            self.initialized = True
            print(self.__dict__, "self")
            print(f"Initializing instance with name: {self.data.get('name')}")

    def __call__(self):
        print("Calling...")
    
    def __del__(self):
   
        print(f"Deleting instance...: {self.data}")

# Test the implementation
if __name__ == "__main__":
    data = {
        "name": "Fawad",
        "age": 20,
        "city": "Karachi"
    }
    p = Example(data)
    b = Example("string")  # This will print error message
    print(f"Are p and b the same instance? {p is b}")  # Will print True

class Singleton:
    _instance = None  # Class variable to store the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # If no instance exists, create one
            cls._instance = super().__new__(cls)
            # Initialize the instance
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not self.initialized:
            # Initialize only if not already initialized
            self.initialized = True
            # Your initialization code here
            self.data = kwargs.get('data', None)

# Example usage
if __name__ == "__main__":
    # Create first instance
    s1 = Singleton(data="First instance")
    print(f"s1 data: {s1.data}")  # Output: s1 data: First instance

    # Try to create second instance
    s2 = Singleton(data="Second instance")
    print(f"s2 data: {s2.data}")  # Output: s2 data: First instance
    print(f"Are s1 and s2 the same instance? {s1 is s2}")  # Output: True
