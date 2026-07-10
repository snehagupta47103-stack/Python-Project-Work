<div align="center">

# 📊 NumPy Analyzer

### A Menu-Driven Python Application for NumPy Array Operations and Data Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-Library-orange?style=for-the-badge&logo=numpy)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-blue?style=for-the-badge&logo=visualstudiocode)
![GitHub](https://img.shields.io/badge/GitHub-Project-black?style=for-the-badge&logo=github)

---

### 🎓 Project 8

**Course:** Python Programming

**Project Title:** NumPy Analyzer

**Language:** Python

**Library Used:** NumPy

**IDE:** Visual Studio Code

---

</div>

# 📑 Table of Contents

- Introduction
- Project Objectives
- Problem Statement
- Features
- Technologies Used
- Project Structure
- Workflow
- Object-Oriented Programming Concepts
- NumPy Functions Used
- Mathematical Operations
- Data Analysis
- Exception Handling
- How to Run
- Expected Output
- Learning Outcomes
- Future Enhancements
- Conclusion

---

# 📖 Introduction

NumPy Analyzer is a menu-driven Python application developed using the **NumPy** library and **Object-Oriented Programming (OOP)** concepts.

The main objective of this project is to perform various array operations and statistical analysis using NumPy while providing a simple and interactive command-line interface.

The application enables users to create **1D, 2D, and 3D arrays**, perform mathematical computations, manipulate arrays, search and sort data, calculate statistical values, and explore various NumPy functions through an easy-to-use menu system.

---

# 🎯 Project Objectives

The objectives of this project are:

- Learn the fundamentals of NumPy.
- Understand multidimensional arrays.
- Implement Object-Oriented Programming.
- Perform mathematical operations on arrays.
- Perform array manipulation using NumPy.
- Compute statistical information.
- Build a menu-driven Python application.
- Apply exception handling for better reliability.

---

# ❓ Problem Statement

Working with numerical data manually can become difficult when the dataset grows larger.

Python's NumPy library provides optimized data structures and functions that simplify numerical computations, matrix operations, and statistical analysis.

This project demonstrates how NumPy can be used to efficiently perform array creation, indexing, slicing, searching, sorting, filtering, mathematical operations, and statistical analysis within a single menu-driven application.

---

# ⭐ Key Features

| Feature | Description |
|---------|-------------|
| 1D Array | Create one-dimensional arrays |
| 2D Array | Create two-dimensional arrays |
| 3D Array | Create three-dimensional arrays |
| Indexing | Access array elements |
| Slicing | Extract required portions of arrays |
| Mathematical Operations | Addition, Subtraction, Multiplication, Division |
| Dot Product | Vector multiplication |
| Matrix Multiplication | Matrix calculations |
| Combine Arrays | Horizontal & Vertical combination |
| Split Arrays | Divide arrays into multiple parts |
| Search | Find required elements |
| Sort | Arrange elements in ascending order |
| Filter | Filter data using conditions |
| Statistics | Mean, Median, Variance, Standard Deviation, Percentile, Correlation |
| Exception Handling | Prevent invalid user inputs |

---

# 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| NumPy | Numerical Computing Library |
| VS Code | Code Editor |

---

# 📁 Project Structure

```
Project-8/
│
├── main.py
├── menu.py
├── data_analytics.py
├── arrays.py
├── operations.py
├── analytics.py
└── README.md
```

---

# 📂 File Description

| File Name | Description |
|------------|-------------|
| **main.py** | Entry point of the application. Controls the complete menu-driven system. |
| **menu.py** | Displays all menus and user options. |
| **data_analytics.py** | Base class implementing Constructor, Private Method, Class Method, and Static Method. |
| **arrays.py** | Handles array creation, indexing, slicing, displaying arrays, and array information. |
| **operations.py** | Performs mathematical operations, dot product, matrix multiplication, combining and splitting arrays. |
| **analytics.py** | Performs searching, sorting, filtering, aggregate functions, and statistical analysis. |
| **README.md** | Documentation of the project. |

---

# 🔄 Project Workflow

```
            Start
               │
               ▼
      Display Main Menu
               │
               ▼
      User Selects Option
               │
     ┌─────────┼─────────┐
     │         │         │
     ▼         ▼         ▼
 Array     Operations  Analytics
     │         │         │
     └─────────┼─────────┘
               ▼
        Display Result
               │
               ▼
      Return to Main Menu
               │
               ▼
             Exit
```

---

# 🏗 Object-Oriented Programming Concepts Used

This project is developed using Object-Oriented Programming principles.

## 1️⃣ Class

Multiple classes are created to organize different functionalities of the project.

Example:

- DataAnalytics
- ArrayOperations
- Operations
- Analytics

---

## 2️⃣ Object

An object of the Analytics class is created inside **main.py** to access all functionalities.

Example:

```python
obj = Analytics()
```

---

## 3️⃣ Constructor

The constructor initializes the array object whenever a new object is created.

Example:

```python
def __init__(self):
    self.array = None
```

---

## 4️⃣ Inheritance

Inheritance is used to reuse code across multiple classes.

```
DataAnalytics
       │
       ▼
ArrayOperations
       │
       ▼
Operations
       │
       ▼
Analytics
```

This avoids code duplication and improves maintainability.

---

## 5️⃣ Private Method

Private methods are used to hide internal implementation details.

Example:

```python
def __display_array(self):
```

This method can only be accessed from inside the class.

---

## 6️⃣ Class Method

Class methods operate on class variables.

Example:

```python
@classmethod
def total_objects(cls):
```

Used to display the total number of objects created.

---

## 7️⃣ Static Method

Static methods perform utility tasks that are not dependent on object data.

Example:

```python
@staticmethod
def project_information():
```

Displays general information about the project.

---

# 📦 NumPy Functions Used

The following NumPy functions are used throughout the project.

| Function | Purpose |
|----------|---------|
| np.array() | Create NumPy arrays |
| np.shape | Returns array shape |
| np.ndim | Returns dimensions |
| np.size | Returns total elements |
| np.dtype | Returns data type |
| np.dot() | Computes dot product |
| np.matmul() | Matrix multiplication |
| np.hstack() | Horizontal combination |
| np.vstack() | Vertical combination |
| np.array_split() | Splits arrays |
| np.where() | Searches elements |
| np.sort() | Sorts arrays |
| np.sum() | Calculates sum |
| np.mean() | Calculates average |
| np.median() | Calculates median |
| np.min() | Finds minimum |
| np.max() | Finds maximum |
| np.std() | Standard deviation |
| np.var() | Variance |
| np.percentile() | Percentile calculation |
| np.corrcoef() | Correlation coefficient |

---

# 🧩 Modules of the Project

The project is divided into five major modules.

### Module 1 — Array Creation

- Create 1D Array
- Create 2D Array
- Create 3D Array

### Module 2 — Array Manipulation

- Display Array
- Array Information
- Indexing
- Slicing

### Module 3 — Mathematical Operations

- Addition
- Subtraction
- Multiplication
- Division
- Dot Product
- Matrix Multiplication

### Module 4 — Array Operations

- Combine Arrays
- Split Arrays

### Module 5 — Data Analysis

- Search
- Sort
- Filter
- Aggregate Functions
- Statistical Analysis

---

# 🔢 Array Creation

Array creation is the first step of this project. The application allows users to create **1D**, **2D**, and **3D** NumPy arrays dynamically by taking input from the keyboard.

---

## 📌 1D Array

A one-dimensional array stores elements in a single row.

### Example

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr)
```

### Sample Output

```
[10 20 30 40 50]
```

### Advantages

- Easy to create
- Less memory consumption
- Faster processing
- Suitable for linear data

---

## 📌 2D Array

A two-dimensional array stores data in rows and columns.

### Example

```python
arr = np.array([[10,20,30],
                [40,50,60]])
print(arr)
```

### Sample Output

```
[[10 20 30]
 [40 50 60]]
```

### Advantages

- Matrix representation
- Row and column operations
- Useful for tables
- Easy indexing

---

## 📌 3D Array

A three-dimensional array consists of multiple matrices.

### Example

```python
arr = np.array([
[[1,2],[3,4]],
[[5,6],[7,8]]
])
print(arr)
```

### Sample Output

```
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
```

### Advantages

- Stores multiple matrices
- Useful for image processing
- Supports higher-dimensional data

---

# 📋 Display Array Information

The project displays complete information about the currently created array.

Information displayed:

- Shape
- Dimension
- Size
- Data Type

### Example

```python
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
```

### Sample Output

```
Shape : (2,3)
Dimension : 2
Size : 6
Data Type : int64
```

---

# 🔍 Array Indexing

Indexing is used to access individual elements of an array.

The project supports indexing for:

- 1D Arrays
- 2D Arrays
- 3D Arrays

### Example

```python
arr = np.array([10,20,30,40])

print(arr[2])
```

### Output

```
30
```

### 2D Example

```python
arr = np.array([[10,20],
                [30,40]])

print(arr[1][0])
```

### Output

```
30
```

---

# ✂️ Array Slicing

Slicing is used to retrieve a specific portion of an array.

### Example

```python
arr = np.array([10,20,30,40,50])

print(arr[1:4])
```

### Output

```
[20 30 40]
```

### 2D Example

```python
arr[:,1]
```

Output

```
[20 40]
```

### Advantages

- Faster than loops
- Easy data extraction
- Memory efficient

---

# ➕ Mathematical Operations

The project performs mathematical operations using NumPy.

Operations included:

- Addition
- Subtraction
- Multiplication
- Division

### Addition

```python
arr + 5
```

Output

```
[15 25 35 45]
```

---

### Subtraction

```python
arr - 5
```

Output

```
[5 15 25 35]
```

---

### Multiplication

```python
arr * 2
```

Output

```
[20 40 60 80]
```

---

### Division

```python
arr / 2
```

Output

```
[5. 10. 15. 20.]
```

---

# 🎯 Dot Product

The project calculates the dot product between two vectors.

Example

```python
a = np.array([1,2,3])

b = np.array([4,5,6])

np.dot(a,b)
```

Output

```
32
```

---

# 🧮 Matrix Multiplication

Matrix multiplication is performed using **np.matmul()**.

Example

```python
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

np.matmul(A,B)
```

Output

```
[[19 22]
 [43 50]]
```

Matrix multiplication is useful in:

- Machine Learning
- Data Science
- Computer Graphics
- Scientific Computing

---
| GitHub | Version Control |

---

# 🔗 Combine Arrays

The project provides functionality to combine two arrays into a single array using NumPy.

The following methods are implemented:

- Horizontal Combination (`np.hstack()`)
- Vertical Combination (`np.vstack()`)

---

## 📌 Horizontal Combination

Horizontal stacking combines arrays column-wise.

### Example

```python
import numpy as np

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print(np.hstack((a,b)))
```

### Output

```
[[1 2 5 6]
 [3 4 7 8]]
```

---

## 📌 Vertical Combination

Vertical stacking combines arrays row-wise.

### Example

```python
import numpy as np

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print(np.vstack((a,b)))
```

### Output

```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

---

# ✂️ Split Arrays

The project also supports splitting arrays into equal parts using NumPy.

### Function Used

```python
np.array_split()
```

### Example

```python
arr = np.array([10,20,30,40,50,60])

print(np.array_split(arr,3))
```

### Output

```
[array([10,20]),
 array([30,40]),
 array([50,60])]
```

---

# 🔍 Search Operation

Searching helps locate a specific value inside an array.

The project uses:

```python
np.where()
```

### Example

```python
arr = np.array([10,20,30,40,50])

print(np.where(arr==30))
```

### Output

```
(array([2]),)
```

---

# 📊 Sort Operation

Sorting arranges array elements in ascending order.

### Function Used

```python
np.sort()
```

### Example

```python
arr = np.array([45,12,67,23,5])

print(np.sort(arr))
```

### Output

```
[ 5 12 23 45 67]
```

---

# 🎯 Filter Operation

Filtering returns elements satisfying a given condition.

### Example

```python
arr = np.array([10,20,30,40,50])

print(arr[arr>25])
```

### Output

```
[30 40 50]
```

Filtering is useful for:

- Data Cleaning
- Data Analysis
- Machine Learning
- Business Analytics

---

# 📈 Aggregate Functions

Aggregate functions summarize numerical data.

The project implements the following aggregate functions.

| Function | Description |
|----------|-------------|
| Sum | Calculates total sum |
| Mean | Calculates average |
| Minimum | Finds smallest value |
| Maximum | Finds largest value |

---

## Sum

```python
np.sum(arr)
```

Output

```
150
```

---

## Mean

```python
np.mean(arr)
```

Output

```
30.0
```

---

## Minimum

```python
np.min(arr)
```

Output

```
10
```

---

## Maximum

```python
np.max(arr)
```

Output

```
50
```

---

# 📉 Statistical Analysis

The NumPy Analyzer project performs various statistical calculations.

Implemented statistical functions include:

- Mean
- Median
- Standard Deviation
- Variance
- Percentile
- Correlation Coefficient

---

## 📌 Median

```python
np.median(arr)
```

Output

```
30.0
```

---

## 📌 Standard Deviation

```python
np.std(arr)
```

Output

```
14.14
```

---

## 📌 Variance

```python
np.var(arr)
```

Output

```
200.0
```

---

## 📌 Percentile

```python
np.percentile(arr,50)
```

Output

```
30.0
```

---

## 📌 Correlation Coefficient

```python
a = np.array([1,2,3,4,5])

b = np.array([2,4,6,8,10])

print(np.corrcoef(a,b))
```

### Output

```
[[1. 1.]
 [1. 1.]]
```

The Correlation Coefficient measures the relationship between two datasets.

- **+1** → Perfect Positive Correlation
- **0** → No Correlation
- **−1** → Perfect Negative Correlation

---

# ⚠️ Exception Handling

The project uses exception handling to make the application more reliable.

Handled exceptions include:

- Invalid menu choice
- Invalid array index
- Invalid numeric input
- Division by zero
- Empty array operations

This ensures the application continues to run smoothly even when incorrect input is provided by the user.

---

# 📊 Results and Observations

The NumPy Analyzer project successfully demonstrates various NumPy operations through a menu-driven Python application.

The project allows users to:

- Create 1D, 2D, and 3D NumPy arrays.
- Perform array indexing and slicing.
- Execute mathematical operations efficiently.
- Perform dot product and matrix multiplication.
- Combine and split arrays.
- Search, sort, and filter array elements.
- Compute aggregate and statistical values.
- Handle invalid inputs using exception handling.

The application provides an easy-to-use interface that makes NumPy concepts simple to understand and implement.

---

# 🚀 Advantages of the Project

| Advantage | Description |
|------------|-------------|
| User Friendly | Simple menu-driven interface for easy navigation. |
| Efficient | NumPy performs operations much faster than traditional Python lists. |
| Reusable | Object-Oriented Programming improves code reusability. |
| Organized | Project is divided into multiple Python modules. |
| Reliable | Exception handling prevents unexpected program crashes. |
| Scalable | New NumPy features can be added easily in the future. |

---

# 🔮 Future Enhancements

The project can be extended by adding more advanced NumPy and data analysis features.

Possible enhancements include:

- Reading datasets from CSV files.
- Saving analysis reports.
- Data visualization using Matplotlib.
- Graphical User Interface (GUI).
- Pandas integration for data analysis.
- Support for larger datasets.
- Exporting statistical reports.

---

# 🎯 Learning Outcomes

After completing this project, the following concepts were understood and implemented successfully:

- Python Programming
- NumPy Library
- Object-Oriented Programming (OOP)
- Constructors
- Inheritance
- Private Methods
- Class Methods
- Static Methods
- Exception Handling
- Array Manipulation
- Matrix Operations
- Statistical Analysis
- Menu-Driven Programming
- Modular Programming

---

# 📸 Sample Program Flow

```
Start
   │
   ▼
Main Menu
   │
   ├── Create Array
   │
   ├── Mathematical Operations
   │
   ├── Combine / Split Arrays
   │
   ├── Search / Sort / Filter
   │
   ├── Statistics
   │
   └── Exit
```

# OUTPUT
<img width="1189" height="837" alt="Screenshot 2026-07-10 113259" src="https://github.com/user-attachments/assets/251d1862-827c-44eb-96fc-ff79a6847339" />
<img width="1241" height="787" alt="Screenshot 2026-07-10 113329" src="https://github.com/user-attachments/assets/73d3c007-de8b-4501-b1c9-2f951a242042" />
<img width="1197" height="893" alt="Screenshot 2026-07-10 113357" src="https://github.com/user-attachments/assets/bfaa5792-25b8-4c0b-b026-248bed31540b" />
<img width="1150" height="652" alt="Screenshot 2026-07-10 113421" src="https://github.com/user-attachments/assets/2e8e6766-e633-4a20-81a7-93d7f6515f37" />
<img width="1144" height="802" alt="Screenshot 2026-07-10 113446" src="https://github.com/user-attachments/assets/659df3ce-1e6e-4306-9fda-2b50db898133" />
<img width="1184" height="807" alt="Screenshot 2026-07-10 113516" src="https://github.com/user-attachments/assets/f2cc3107-cb76-4df8-8763-00776ee89104" />
<img width="1075" height="910" alt="Screenshot 2026-07-10 113709" src="https://github.com/user-attachments/assets/d5a1e467-0d22-45ca-8343-45b1f8b4d3bc" />
<img width="1131" height="811" alt="Screenshot 2026-07-10 113730" src="https://github.com/user-attachments/assets/a6ac9a7f-1f80-477b-b844-fdb821b8f3f4" />
<img width="1176" height="884" alt="Screenshot 2026-07-10 113753" src="https://github.com/user-attachments/assets/34bb10e1-cd22-4e9a-a4b2-34151609f531" />


---

# 📌 Conclusion

NumPy Analyzer is a complete menu-driven Python application that demonstrates the practical use of the NumPy library for array manipulation, mathematical computation, and statistical analysis.

The project combines Object-Oriented Programming concepts with NumPy functions to create an organized, reusable, and user-friendly application.

This project provides a strong foundation for learning numerical computing and data analysis using Python.

---

# 📜 License

This project is developed for **educational purposes** as part of the Python Programming coursework.

It may be used for learning, practice, and academic demonstrations.

---

# 👨‍💻 Author

**Author Name:** Sneha Gupta

**Project Title:** NumPy Analyzer

**Project:** Project-8

**Language:** Python

**Library:** NumPy

**IDE:** Visual Studio Code

**Version:** 1.0

---

# 🙏 Acknowledgements

Special thanks to:

- Faculty members for their guidance.
- Python Documentation.
- NumPy Documentation.
- Visual Studio Code.
- GitHub for version control.

Their resources and documentation helped in the successful completion of this project.

---

<div align="center">

## ⭐ Thank You for Visiting This Repository ⭐

If you found this project helpful, consider giving it a ⭐ on GitHub.

**Happy Coding! 🚀**

</div>
