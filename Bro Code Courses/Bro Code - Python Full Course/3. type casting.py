# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Laczkovics András Gergő"
age = 18
gpa = 4.67
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

name = bool(name)
age = float(age)
age = str(age)
gpa = int(gpa)

print(name)
print(age)
print(type(age))
print(gpa)