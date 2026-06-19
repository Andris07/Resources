# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

# fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
print(numbers)

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

even_nums = [num for num in numbers if num%2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if num%2 == 1]
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
print(grades)

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)