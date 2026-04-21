
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks 🐶")


class Cat(Animal):
    def sound(self):
        print("Cat meows 🐱")



class Math:
    def add(self, a, b, c=0):   
        return a + b + c



if __name__ == "__main__":

    print("🔹 Method Overriding")
    a1 = Dog()
    a2 = Cat()
    a1.sound()
    a2.sound()

    print("\n🔹 Method Overloading")
    m = Math()
    print(m.add(2, 3))    
    print(m.add(2, 3, 4))    
