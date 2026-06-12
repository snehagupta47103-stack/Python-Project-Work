print("\n--- Python OOP Project: Employee Management System ---\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def display(self):
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

print("Manager subclass of Employee:", issubclass(Manager, Employee))

persons = []
employees = []
managers = []

while True:
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        p = Person(name, age)
        persons.append(p)

        print(f"\nPerson created with Name: {name}, Age: {age}.\n")

    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        e = Employee(name, age, emp_id, salary)
        employees.append(e)

        print(f"\nEmployee created with Name: {name}, Age: {age}, Employee ID: {emp_id}, Salary: {salary}.\n")

    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        m = Manager(name, age, emp_id, salary, department)
        managers.append(m)

        print(f"\nManager created with Name: {name}, Age: {age}, Employee ID: {emp_id}, Salary: {salary}, Department: {department}.\n")

    elif choice == "4":
        print("1. Show Persons")
        print("2. Show Employees")
        print("3. Show Managers")

        show_choice = input("Enter your choice: ")

        if show_choice == "1":
            print("\n----- PERSONS -----")
            for p in persons:
                p.display()

        elif show_choice == "2":
            print("\n----- EMPLOYEES -----")
            for e in employees:
                e.display()

        elif show_choice == "3":
            print("\n----- MANAGERS -----")
            for m in managers:
                m.display()

        else:
            print("\nInvalid Choice\n")

    elif choice == "5":
        print("\nThank you for using Employee Management System.")
        print("Exiting the system.....\n")
        break

    else:
        print("Invalid Choice")
