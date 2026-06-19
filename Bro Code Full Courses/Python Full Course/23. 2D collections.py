fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ("celery", "carrots", "potatoes")
meats =         {"chicken", "fish", "turkey"}

# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]],

groceries = [fruits, vegetables, meats]

# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
# print(groceries[0][0])
# print(groceries[1][1])
# print(groceries[2][2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()