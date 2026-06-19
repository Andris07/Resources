# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals =  {
                "USA": "Washington D.C.",
                "India": "New Delhi",
                "China": "Beijing",
                "Russia": "Moscow",
            }

# print(capitals.get("USA"))    -> Washington D.C.
# print(capitals.get("Japan"))  -> None

exists = capitals.get("Japan")
if exists:
    print("That capital exists")
else:
    print("That capital doesn't exist")
print()

capitals.update({"Germany" : "Berlin"})
capitals.update({"China" : "Peking"})

# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

keys = capitals.keys()
for key in keys:
    print(key)
print()

values = capitals.values()
for value in values:
    print(value)
print()

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")