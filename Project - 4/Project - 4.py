data = []
matrix = []
summary = []

def input_1d():
    "Input 1D Array"
    global data, summary

    nums = input("Enter numbers separated by space: ").split()
    data = []
    for i in nums:
        data.append(int(i))
    summary = {"Count":len(data)}

def input_2d():
    "Input 2D Array"
    global matrix

    rows = int(input("Enter number of rows: "))
    matrix = []
    for i in range(rows):
        row = []
        nums = input("Enter row values: ").split()
        for j in nums:
            row.append(int(j))
        matrix.append(row)

def show_summary():
    "Display Summary"
    if len(data) == 0:
        print("No Data")
        return
    print("Length =", len(data))
    print("Sum =", sum(data))
    print("Minimum =", min(data))
    print("Maximum =", max(data))

def show_args(*args):
    "Demo of *args"
    print("Values received:")
    for i in args:
        print(i,end=" ")
    print()

def show_kwargs(**kwargs):
    "Demo of **kwargs"
    for key, value in kwargs.items():
        print(key,"=",value)

def factorial(n):
    "Factorial using Recursion"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def lambda_demo():
    "Lambda Function Demo"
    square = lambda x: x * x
    num = int(input("Enter a number: "))
    print("Square =",square(num))

def statistics():
    "Return Multiple Values"
    return min(data), max(data)

def sort_data():
    "Sort Arrays"
    if data:
        data.sort()
        print("Sorted 1D Array:", data)

    if matrix:
        sorted_matrix = sorted(matrix)
        print("Sorted 2D Array:")
        for row in sorted_matrix:
            print(row)

def show_docs():
    "Display Function Documentation"
    print(input_1d.__doc__)
    print(input_2d.__doc__)
    print(show_summary.__doc__)
    print(show_args.__doc__)
    print(show_kwargs.__doc__)
    print(factorial.__doc__)
    print(lambda_demo.__doc__)

while True:
    print("\n----------MENU----------")
    print("1. Input 1D Array")
    print("2. Input 2D Array")
    print("3. Display Summary")
    print("4. *args Demo")
    print("5. **kwargs Demo")
    print("6. Factorial (Recursion)")
    print("7. Lambda Function")
    print("8. Global Variable")
    print("9. Return Multiple Values")
    print("10. Sorting")
    print("11. Display 2D Array")
    print("12. Show Documentation")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        input_1d()
        print("Data has been stored successfully")

    elif choice == "2":
        input_2d()
        print("Data has been stored successfully")

    elif choice == "3":
        show_summary()

    elif choice == "4":
        show_args(*data)

    elif choice == "5":
        show_kwargs(Count=len(data),Total=sum(data))

    elif choice == "6":
        n = int(input("Enter Number: "))
        print("Factorial =", factorial(n))

    elif choice == "7":
        lambda_demo()

    elif choice == "8":
        print("Global Variable =", summary)

    elif choice == "9":
        if data:
            minimum, maximum = statistics()
            print("Minimum =", minimum)
            print("Maximum =", maximum)
        else:
            print("No Data")

    elif choice == "10":
        sort_data()

    elif choice == "11":
        for row in matrix:
            print(row)

    elif choice == "12":
        show_docs()

    elif choice == "13":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")




































    






































