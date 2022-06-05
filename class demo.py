class Pet():
    #meathods are subroutines within a class:
    def __init__(self, name, age, color, animal):
        #properties or attributes: 
        self.__name = name
        self.__age = age
        self.__color = color
        self.__animal = animal

p1 = Pet("Snoopy", 15, "black", "dog")
p2 = Pet("Garfield", 10, "Orange", "cat")
print(p2.name)