# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quaks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True

    def speak(self):
        print("HONK!")

dog = Dog()
cat = Cat()
car = Car()

animals = [dog, cat, car]

for animal in animals:
    animal.speak()
    print(animal.alive)