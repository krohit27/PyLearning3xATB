# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior

def my_deco(func):
    def wrapper():
        print("Starting.....")
        print("****************")
        func()
        print("****************")
        print("Ending")

    return wrapper()


@my_deco
def say_hello():
    print("Say Hello")

