class Employee:
    def __init__(self, name, salary):
        self.__name = name          
        self.__salary = salary     


    @property
    def name(self):
        return self.__name

    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive")

    
    def give_bonus(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Bonus added ₹{amount}. New salary: ₹{self.__salary}")
        else:
            print("Bonus must be positive")



if __name__ == "__main__":

    name = input("Enter employee name: ")
    salary = float(input("Enter initial salary: "))

    emp = Employee(name, salary)

    print(f"Employee: {emp.name}, Salary: ₹{emp.salary}")

    bonus = float(input("Enter bonus amount: "))
    emp.give_bonus(bonus)

    new_salary = float(input("Enter updated salary: "))
    emp.salary = new_salary

    print(f"Updated Salary: ₹{emp.salary}")
