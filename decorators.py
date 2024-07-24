# what are decorators in python?
# A decorator is a function that takes another function as an argument,
# adds some functionality, and returns another function.

# Python decorators are a powerful and flexible way to modify the behavior of 
# functions or methods. They allow you to "wrap" a function, 
# adding some functionality before or after the main function execution,
# without modifying the function itself.
# This is achieved by defining a function that returns another function.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# now lets have a decorator that allow odd numbers to print out
print("----------------------------------------\n")

def odd_numbers_only(func):
    def filter_odd_num(num):
        if num % 2 == 0:
            print("even numbers are not allowed!")
        else:
            func(num)
    return filter_odd_num

@odd_numbers_only
def display_numbers(num):
    print(num)
    
for num in range(1,7):
    display_numbers(num)
    