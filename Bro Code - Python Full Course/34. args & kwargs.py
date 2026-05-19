# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Squarepants", "III")

def print_address(**kwargs):
    # for key in kwargs.keys():
    #     print(key)
    # for value in kwargs.values():
    #     print(value)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", apt="100", city="Detroit", state="MI", zip=54321)