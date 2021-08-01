"""
    What's happening inside the hood
    we have something called stack memory. 
    when we call recursive method(4) 
    if first checks, if 4 < 1 , since 4 is not less than 1,
    it goes to else section and calls the recursive method(3),
    but we still have print(4) to be executed , but it won't be executed until recursive method (3) is completed to give back the control to 
    recursive method(4)

    recursivemethod(0) -> print 0 is less than 1 , and give the control back to recursivemethod(1)
    recursivemethod(1) -> print(1) is waiting to be executed, once the recursivemethod(0) is completed , then print(1) will be executed.
    recursivemethod(2) -> print(2) is waiting to be executed, once the recursivemethod(1) is completed, then print(2) will be executed.
    recursivemethod(3) -> print(3) is waiting to be executed, once the recursivemethod(2) is completed, then print(3) will be executed.
    recursivemethod(4) -> print(4) is waiting to be executed, once the recursivemethod(3) is completed, then print(4) will be executed.
"""

def recursive_method(n):
    if n < 1:
        print(f"{n} is less than 1")
    else:
        recursive_method(n-1)
        print(n)

recursive_method(4)


# another example to show a method that computes the power of 2 using recursion and iteration

"""
    power_of_2_recursively(0) - returns 1
    power_of_2_recursively(1) - waits for power * 2 to be executed after power_of_2_recursively(0) is completed , when power_of_2_recursively(0) is completed, it returns 1 
                                so now power becomes 1*2
    power_of_2_recursively(2) - waits for power * 2 to be executed after power_of_2_recursively(1) is completed
                                so now power becomes 1*2 * 2 
    power_of_2_recursively(3) - waits for power * 2 to be executed after power_of_2_recursively(2) is completed
                                so now power becomes 1*2*2 *2
    power_of_2_recursively(4) - waits for power * 2 to be executed after power_of_2_recursively(3) is completed 
                                so now it becomes 1*2*2*2 *2
    power_of_2_recursively(5) - waits for power * 2 to be executed after power_of_2_recursively(4) is completed
                                so now it becomes 1*2*2*2*2 *2
"""
def power_of_2_recursively(n):
    if n == 0:
        return 1
    else:
        power = power_of_2_recursively(n-1)
        return power * 2

def power_of_2_iteratively(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
    return power

print(f"The power of 8 recursively: {power_of_2_recursively(5)}")
print(f"The power of 8 iteratively: {power_of_2_iteratively(5)}")


# Let's consider another example of factorial to write recursively
"""
    for example, consider the factorial equation below:
    n! = n * (n-1) * (n-2) * (n-3) * ... * 2 * 1
    n! = n * (n-1)!
"""

def factorial(n):
    assert n >= 0 and int(n) == n, 'Wrong Input: Factorial is only supported for integer values'
    if n in [0, 1]:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact

print(f"The factorial of number 5 is : {factorial(3)}")

# Lets consider another example : fibonacci. 
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ,...
# Step 1 - Identify RECURSIVE case
    # 5 = 3 + 2
    # f(n) = f(n-1) + f(n-2)   
# Step 2 - Identify BASE case
    #fib(0) = 0 
    #fib(1) = 1
# Step 3 - Consider different types of input values

def fibonacci(n):
    assert n >=0 and int(n) == n , "Fibonacci is not supported for number < 0"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(f"The fibonacci of the number is :{fibonacci(7)}")