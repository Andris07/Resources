# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and immutable. Duplicates OK. FASTER

# LIST
# fruits = ["apple", "orange", "banana", "coconut"]

# print(len(fruits))
# print(fruits[0])
# fruits[0] = "pineapple"
# print("pineapple" in fruits)
# fruits.append("watermelon")
# fruits.remove("watermelon")
# fruits.insert(0, "watermelon")
# fruits.sort()
# fruits.reverse()
# fruits.index("pineapple")
# fruits.count("pineapple")
# fruits.clear()

# SET
# fruits = {"apple", "orange", "banana", "coconut"}

# fruits.add("pineapple")
# fruits.remove("pineapple")
# fruits.pop()
# fruits.clear()

# TUPLE
fruits = ("apple", "orange", "banana", "coconut")

# print(fruits)
# for fruit in fruits:
#     print(fruit)