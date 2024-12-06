def decorator(func):
    def wrapper():
        print("1st")
        func()
        print("3rd")
    return wrapper
    
@decorator    
def say_hi():
    print("2nd")
say_hi()    