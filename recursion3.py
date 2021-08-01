# find the gcd of two numbers using recursion

def gcd_of_two_numbers(a, b):
    assert a>=0 and b >=0 and int(a) == a and int(b) == b, "not supported for negative integers"
    if b == 0:
        return a
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b 
    return gcd_of_two_numbers(int(b), int(a % b))

print(f"The GCD of 48, 18 is {gcd_of_two_numbers(48, 18)}")