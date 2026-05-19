# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)
print("10 is the first double digit number\n")

for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!\n")

for x in range(1, 11, 2):
    print(x)
print("Odd single digit numbers\n")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)
print("Credit card numbers\n")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
print("Skipping 13\n")

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
print("Breaking at 13\n")