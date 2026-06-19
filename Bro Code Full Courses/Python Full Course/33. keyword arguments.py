# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# hello("Mr.", "Hello", "Spongebob", "Squarepants") # Mr. Hello Spongebob Squarepants -> wrong order of variables
hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")
hello("Hello", first="Spongebob", last="Squarepants", title="Mr.")
# hello(first="Spongebob", last="Squarepants", title="Mr.", "Hello") -> "Positional argument cannot appear after keyword arguments" error message

hello("Hello", title="Mr.", last="John", first="James")

for x in range(1, 11):
    print(x, end=" ")
print()

print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+36", area="30", first="954", last="5224")

print(phone_num)