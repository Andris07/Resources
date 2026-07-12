# Code Example #01
def walk(steps):
    # Base case
    if steps < 1:
        return

    print("You take a step")

    # Recursive case
    walk(steps-1)

# Code Example #02
def factorial(num):
    if num < 1:
        return 1
    
    return num * factorial(num - 1)

# Code Example #03
def power(base, exponent):
    if exponent < 1:
        return 1
    
    return base * power(base, exponent-1)

walk(5)
print()
print(factorial(7))
print()
print(power(2, 8))