# find the power of a positive number

def power_of_a_number(base, exp):
    assert exp >= 0 and int(exp) == exp, "negative exponent not supported"
    if exp == 0 :
        return 1
    if exp == 1:
        return base
    return base * power_of_a_number(base, exp - 1)

print(f"{power_of_a_number(2,4)}")