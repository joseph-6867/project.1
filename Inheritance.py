# 1️⃣ SINGLE INHERITANCE
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):  
    def bark(self):
        print("Dog barks")
      
# 2️⃣ MULTILEVEL INHERITANCE
class GrandFather:
    def house(self):
        print("GrandFather's house")

class Father(GrandFather):  
    def car(self):
        print("Father's car")

class Son(Father):  
    def bike(self):
        print("Son's bike")

# 3️⃣ MULTIPLE INHERITANCE
class Programmer:
    def code(self):
        print("Writes code")

class Youtuber:
    def make_video(self):
        print("Makes YouTube videos")

class TechBoy(Programmer, Youtuber):  
    def earn(self):
        print("Earns from both coding & YouTube")

# 4️⃣ HIERARCHICAL INHERITANCE
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):   
    def car_info(self):
        print("This is a car")

class Bike(Vehicle):  
    def bike_info(self):
        print("This is a bike")



print("\n--- 1️⃣ SINGLE INHERITANCE ---")
d = Dog()
d.eat()
d.bark()

print("\n--- 2️⃣ MULTILEVEL INHERITANCE ---")
s = Son()
s.house()
s.car()
s.bike()

print("\n--- 3️⃣ MULTIPLE INHERITANCE ---")
t = TechBoy()
t.code()
t.make_video()
t.earn()

print("\n--- 4️⃣ HIERARCHICAL INHERITANCE ---")
c = Car()
b = Bike()
c.start()
c.car_info()
b.start()
b.bike_info()
