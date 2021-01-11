# In this code we will revise some fundamental properties of functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# Idea 1: functions can be passed as parameters/input to functions
def apply(func, a, b):
    return func(a, b)

# Idea 2: functions can also return functions as output
def power(n):
    def func(number):
        return number**n
    return func

# function as input
print(apply(add,2,-3))
print(apply(sub,2,-3))

# function as output
pow2 = power(2)
pow3 = power(3)

print(pow2(3))
print(pow3(4))

# combining two ideas
import time
import random

def stopwatch(f):
    def func():
        tic = time.time()
        result = f()    # run the function passed in the parameter
        print("this function took {} seconds to run.".format(time.time() - tic))
        return result # return the function
    return func

def sleep_random():
    time.sleep(random.random())
    return "Done!"

# this aspect of decorating a function can be handled by using
# the @ operator
timed_sleep = stopwatch(sleep_random)

print(sleep_random())
print(timed_sleep())

# now the sleep_random_2 function is decorated by stopwatch
@stopwatch
def sleep_random_2():
    time.sleep(random.random())
    return "Done!"

print(sleep_random_2())