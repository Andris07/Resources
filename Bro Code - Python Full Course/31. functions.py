# function = A block of reusable code
#            place () after the function name to invoke it

# return =   statement used to end a function
#            and send a result back to the caller

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to you!")
    print()

happy_birthday("Andrew", 18)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due {due_date}")
    print()

display_invoice("iqletandrew73", 41.67, "06/07")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiple(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiple(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = first.capitalze()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)