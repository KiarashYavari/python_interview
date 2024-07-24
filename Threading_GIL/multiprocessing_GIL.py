# process: A process is an independent program
# in execution with its own memory space.

# thread: A thread (also known as a lightweight process) 
# is a smaller unit of a process that can run concurrently.
# Multiple threads can exist within the same process and 
# share the same memory space.

# GIL: preventing multiple threads from executing Python bytecodes at once.
# This means that even if you have multiple threads in a Python program,
# only one thread can execute Python code at a time per process.

# CPU-bound tasks: The GIL can be a bottleneck for CPU-bound tasks,
# where the program needs to perform a lot of computations.
# In such cases, multithreading might not improve performance because 
# the threads are competing for the GIL.

# A typical CPU-bound task could be calculating the Fibonacci sequence 
# for a large number of elements.
import multiprocessing
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_worker(n):
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")

# The if __name__ == "__main__": construct ensures that the process creation 
# and execution code runs only when the module is executed directly,
# not when it is imported and functions from it are called.

# it is essential in multi processing to do this and prevents the child process
# from re-importing the script and running the process creation code again,
# which would lead to an infinite loop.

if __name__ == '__main__':
    numbers = [35, 36, 37, 38] # Larger numbers to demonstrate CPU-bound tasks
    processes = []

    start_time = time.time()
    
    for number in numbers:
        process = multiprocessing.Process(target=fibonacci_worker, args=(number,))
        processes.append(process)
        process.start()

# Using join() ensures that the main program waits for
# all processes to complete, leading to predictable and 
# correct program execution.

    for process in processes:
        process.join()
        
    end_time = time.time()
    print(f"Calculation completed in {end_time - start_time} seconds")
    