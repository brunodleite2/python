def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        "Decorator Hook"

        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    
    print(x, end=" ")
    print(y)
    return x * y

print(product(3, 2))