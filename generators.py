# generators are a simple and powerful tool for creating iterators. 
# They allow you to iterate over a sequence of
# values without creating the entire sequence in memory at once, 
# which is useful for large datasets or streams of data.

# A generator function is defined like a normal function
# but uses the yield statement to return values one at a time, 
# pausing the function’s state between each call. 
# When yield is used in a function,
# it automatically makes the function a generator.

# Iteration: Each call to next() on the generator
# resumes execution until it hits the next yield statement.

def first_generator():
    yield 1
    yield 2
    yield 3
    
first_gen_obj = first_generator()

# iterate over generator
print(next(first_gen_obj)) # 1
print(next(first_gen_obj)) # 2
print(next(first_gen_obj)) # 3

# good example of generators in python --> creating fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
fibo_gen_obj = fibonacci_generator()

# create first 10 numbers of fibonucci sequence

for i in range(10):
    print(next(fibo_gen_obj))
    
# Key Points:

# Memory Efficiency: Generators do not store the entire sequence in memory. 
# They generate each value on the fly.

# Lazy Evaluation: Values are computed only when requested,
# making generators suitable for large or infinite sequences.

# Simpler Code: Using yield makes it easy to write iterators
# without needing to manage the internal state and control flow manually.

