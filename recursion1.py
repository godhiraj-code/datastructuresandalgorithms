# Find sum of digits of a positive integer number using recursion
# Step 1 : Identify the recursive flow
# 10  = 1 + 0 = 1 
# 10 / 10 = 1 and remainder = 0 
# 54 / 10  = 5 and remainder = 4 
# 112 / 10 = 11 and remainder = 2 
# 11/10 = 1 and remainder = 1
# f(n) = f(n% 10) + f (n/10)
# Step 2 : Find the base condition
# Step 3 : Check the all types of input files

def sum_of_digit(n):
    assert n >= 0 and int(n) == n, 'Not supported for non negative digits'
    if n == 0:
        return n
    return int(n%10) + sum_of_digit(int(n/10))

print(f"sum of digits : {sum_of_digit(4)}")



