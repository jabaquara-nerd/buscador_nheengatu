class Person:
    name = "undefined"
    age = 0

    def __init__(self, nome, idade):
        self.name = nome
        self.age = idade

    def __repr__(self):
        return f"Person name: ({self.age}) {self.name} "


andre = Person("Andre Wesley", 99)
print(andre)
will = Person("Will Uiu", 1000)
print(will)
