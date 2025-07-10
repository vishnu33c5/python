class Animal:
    def  make_sound(self):
        print("Making sound")
class Dog(Animal):
    def make_sound(self):
        print("Making dog noice")
class Cat(Animal):
    def make_sound(self):
        print("Making cat noice")
for b in (Dog(),Cat()):
    b.make_sound()