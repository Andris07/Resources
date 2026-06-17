# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = "Andris"
food = "Mexikói Chilis Bab"
email = "laczkovicsandris07.programming@gmail.com"

print(f"Hello {first_name}")
print(f"You like: {food}")
print(f"Your email is: {email}")

# Integers
age = 18
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Floats
price = 13.67
gpa = 4.67
distance = 6.7

print(f"The price is: ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km")

# Booleans
is_student = True
for_sale = False
is_online = True

if is_student:
  print("You are a student")
else:
  print("You are NOT a student")

if for_sale:
  print("That item is for sale")
else:
  print("That item is NOT available")

if is_online:
  print("You are online")
else:
  print("You are offline")