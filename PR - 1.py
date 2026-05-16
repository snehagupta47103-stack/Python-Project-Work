print("Welcome to personal data collector")

name = input("Enter your name :")
age = int(input("Enter your age :"))
height = float(input("Enter your height in meters:"))
fav_num = int(input("Enter your favourite number:"))

birth_year = 2023 - age
height_int = int(height)

print("Thank you! Here is the information we collected:")

print(name,type(name),id(name))
print(age,type(age),id(age))
print(height,type(height),id(height))
print(fav_num,type(fav_num),id(fav_num))

print(f"Your birth year is approximately : {birth_year}")
print(f"(Based on your age of {age})")
print(f"Note: Your height was converted from float {height} to integer {height_int} for rounding.")
print("Thank you for using the personal data collector. Goodbye!")
