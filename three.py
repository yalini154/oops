class Dog:
    species = "Dogs"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Buddy = Dog("Buddy",11)
Max = Dog("Max", 5)
print("Buddy is a {}".format(Buddy.species))
print("Max is also a {}".format(Max.species))
print("{} is {} years old".format(Buddy.name, Buddy.age))
print("{} is {} years old".format(Max.name, Max.age))