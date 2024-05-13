class Cat:

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour


class Kitten(Cat):
    pass

    def personality(self):
        return "curious" + self.name

    def walk(self):
        return "sneak" + self.name


c1 = Cat("Milo", 12, "red")
print(c1.name)
print(c1.colour)
