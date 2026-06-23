import datetime
import time
import math
import random
import uuid
import string

def display_current_datetime():
    now = datetime.datetime.now()
    print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def date_difference():
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

    diff = abs((d2 - d1).days)
    print(f"Difference: {diff} days")


def format_date():
    date_str = input("Enter date (YYYY-MM-DD): ")
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    print("Formatted Date:", d.strftime("%d %B %Y"))


def stopwatch():
    input("Press Enter to start stopwatch...")
    start = time.time()

    input("Press Enter to stop stopwatch...")
    end = time.time()

    print(f"Elapsed Time: {round(end-start, 2)} seconds")


def countdown_timer():
    seconds = int(input("Enter countdown seconds: "))

    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_current_datetime()

        elif choice == "2":
            date_difference()

        elif choice == "3":
            format_date()

        elif choice == "4":
            stopwatch()

        elif choice == "5":
            countdown_timer()

        elif choice == "6":
            break

        else:
            print("Invalid choice")

def factorial_calculation():
    num = int(input("Enter a number: "))
    print("Factorial:", math.factorial(num))


def compound_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (in %): "))
    years = float(input("Enter time (in years): "))

    amount = principal * ((1 + rate / 100) ** years)

    print(f"Compound Interest: {amount:.2f}")


def trigonometry():
    angle = float(input("Enter angle in degrees: "))

    rad = math.radians(angle)

    print("Sin:", round(math.sin(rad), 4))
    print("Cos:", round(math.cos(rad), 4))
    print("Tan:", round(math.tan(rad), 4))


def area_shapes():

    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area:", round(math.pi * r * r, 2))

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area:", l * w)

    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area:", 0.5 * b * h)


def math_menu():
    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            factorial_calculation()

        elif choice == "2":
            compound_interest()

        elif choice == "3":
            trigonometry()

        elif choice == "4":
            area_shapes()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

def random_number():
    print("Random Number:", random.randint(1, 100))


def random_list():
    numbers = []

    for _ in range(5):
        numbers.append(random.randint(1, 100))

    print("Random List:", numbers)


def random_password():
    length = int(input("Enter password length: "))

    chars = string.ascii_letters + string.digits + "!@#$%&*"

    password = ""

    for _ in range(length):
        password += random.choice(chars)

    print("Generated Password:", password)


def random_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)


def random_menu():
    while True:

        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_number()

        elif choice == "2":
            random_list()

        elif choice == "3":
            random_password()

        elif choice == "4":
            random_otp()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

def generate_uuid():
    print("\nGenerated UUID:", uuid.uuid4())

def create_file():
    filename = input("Enter file name: ")

    file = open(filename, "w")
    file.close()

    print("File created successfully!")


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    file = open(filename, "w")
    file.write(data)
    file.close()

    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ")

    file = open(filename, "r")

    print("File Content:")
    print(file.read())

    file.close()


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    file = open(filename, "a")
    file.write(data)
    file.close()

    print("Data appended successfully!")


def file_menu():
    while True:

        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_file()

        elif choice == "5":
            break

def explore_module():

    module_name = input("Enter module name to explore: ")

    if module_name == "math":
        print("\nAvailable Attributes in math module:")
        print(dir(math))

    elif module_name == "random":
        print("\nAvailable Attributes in random module:")
        print(dir(random))

    elif module_name == "datetime":
        print("\nAvailable Attributes in datetime module:")
        print(dir(datetime))

    elif module_name == "uuid":
        print("\nAvailable Attributes in uuid module:")
        print(dir(uuid))

    else:
        print("Module not supported")

def main():

    while True:

        print("\n========================")
        print("Welcome to Multi-Utility Toolkit")
        print("========================")

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\n========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("========================")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()