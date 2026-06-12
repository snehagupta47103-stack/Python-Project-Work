# Employee Management System

### Interactive Console-Based Employee Record Management Using Object-Oriented Programming

---

## 📋 Table of Contents

* Overview
* Problem Statement
* Key Features
* Project Structure
* Project Workflow
* Class Hierarchy
* OOP Concepts Used
* Menu Options
* Sample Output
* Tech Stack
* Advantages
* Author

---

# 📌 Overview

The Employee Management System is a menu-driven Python application developed using Object-Oriented Programming (OOP) principles. The system allows users to create and manage Person, Employee, and Manager records through an interactive command-line interface.

The project demonstrates the practical implementation of inheritance, encapsulation, constructors, destructors, getter/setter methods, method overriding, and parent-child class relationships.

---

# 🎯 Problem Statement

Develop a console-based Employee Management System that allows users to:

* Create Person records
* Create Employee records
* Create Manager records
* Display stored records
* Demonstrate Object-Oriented Programming concepts

The objective is to design a structured system that follows OOP principles while providing a simple menu-driven user experience.

---

# ✨ Key Features

| Feature               | Description                                         |
| --------------------- | --------------------------------------------------- |
| Create Person         | Add a new person record                             |
| Create Employee       | Add a new employee record                           |
| Create Manager        | Add a new manager record                            |
| Show Details          | Display stored records                              |
| Encapsulation         | Employee ID and Salary stored as private attributes |
| Getter/Setter Methods | Controlled access to private data                   |
| Inheritance           | Employee inherits Person, Manager inherits Employee |
| Method Overriding     | Manager overrides display() method                  |
| Menu Driven Interface | Interactive command-line menu                       |
| OOP Implementation    | Demonstrates major OOP concepts                     |

---

# 🏗️ Project Structure

```text
Employee_Management_System/
│
├── Project_5.py
└── README.md
```

---

# 🔄 Project Workflow

```text
Start Program
      │
      ▼
Display Menu
      │
      ▼
┌─────────────────────┐
│ 1. Create Person    │
│ 2. Create Employee  │
│ 3. Create Manager   │
│ 4. Show Details     │
│ 5. Exit             │
└─────────┬───────────┘
          │
          ▼
Create / Store Records
          │
          ▼
Display Requested Data
          │
          ▼
Return to Menu
          │
          ▼
Exit Program
```

---

# 🏛️ Class Hierarchy

```text
Person
   │
   └── Employee
           │
           └── Manager
```

---

# 🧠 OOP Concepts Used

## Constructor

Used to initialize object attributes during object creation.

## Destructor

Used for object cleanup through the **del**() method.

## Encapsulation

Employee ID and Salary are stored as private attributes.

## Getter and Setter Methods

Used to access and update private attributes safely.

## Inheritance

* Employee inherits from Person
* Manager inherits from Employee

## Method Overriding

Manager class overrides the display() method inherited from Employee.

## super()

Used to access parent class constructors and methods.

## issubclass()

Used to verify inheritance relationships between classes.

---

# 📋 Menu Options

```text
1. Create Person
2. Create Employee
3. Create Manager
4. Show Details
5. Exit

```

# Sample Output

<img width="1265" height="766" alt="Screenshot 2026-06-12 193402" src="https://github.com/user-attachments/assets/d3e12878-a4eb-4a15-8952-87135549855d" />
<img width="1351" height="787" alt="Screenshot 2026-06-12 193427" src="https://github.com/user-attachments/assets/b409ad76-7b3b-444a-ac2c-e2b53cbd284b" />
<img width="1248" height="805" alt="Screenshot 2026-06-12 193511" src="https://github.com/user-attachments/assets/5f50b0d8-2067-4b67-9a30-7138da2bb23c" />
<img width="1092" height="768" alt="Screenshot 2026-06-12 193531" src="https://github.com/user-attachments/assets/66157f93-2e78-40df-9cfa-24b932cb83c9" />

---

# 🛠️ Tech Stack

| Tool              | Purpose              |
| ----------------- | -------------------- |
| Python 3.x        | Programming Language |
| OOP Concepts      | System Design        |
| print()           | Console Output       |
| input()           | User Input           |
| Lists             | Record Storage       |
| Classes & Objects | Data Modeling        |

---

# 🏆 Advantages

* Easy to understand and use
* Demonstrates core OOP concepts
* Menu-driven user interface
* Reusable and maintainable code structure
* Suitable for academic OOP projects
* Lightweight and dependency-free

---

# 👤 Author

Name: GUPTA SNEHA

Course: Python Programming

Project Title: Employee Management System

---

# 📌 Conclusion

This project successfully demonstrates the implementation of Object-Oriented Programming concepts in Python through a practical Employee Management System. The application provides a structured approach to managing Person, Employee, and Manager records while maintaining clean code organization and proper OOP design principles.
