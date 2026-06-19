# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]
# numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)
print()

for number in numbers:
    print(number, end=" ")
print("\n")

for number in reversed(numbers):
    print(number)
print()

for number in reversed(numbers):
    print(number, end=" ")
print("\n")

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)
print()

# for fruit in reverse(fruits):
#     print(fruit)
# sets are not reversable

name = "Bro Code"

for character in name:
    print(character, end=" ")
print("\n")

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key in my_dictionary.keys():
    print(key)
print()

for value in my_dictionary.values():
    print(value)
print()

for key, value in my_dictionary.items():
    print(f"{key} = {value}")