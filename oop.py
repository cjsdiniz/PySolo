print("\n\n*** OOP ***")
print("\n#1")


class Cat:

    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print("\n#2")


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
print(felix.color)

print("\n#3")


class Student:
    def __init__(self, name):
        self.name = name


test = Student("Bob")
print(test.name)

print("\n#4")


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

print("\n#5")


class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

print("\nInheritance")
print("\n#1")


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

print("\n# 2")


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


husky = Dog("Max", "grey")
husky.bark()

print("\n# 3")


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()
