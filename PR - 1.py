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

/*
output :-
Welcome to personal data collector
Enter your name : Gupta Sneha 
Enter your age :17
Enter your height in meters: 1.68
Enter your favourite number: 24
Thank you! Here is the information we collected:
 Gupta Sneha  <class 'str'> 2172749973808
17 <class 'int'> 140706051966584
1.68 <class 'float'> 2172791113008
24 <class 'int'> 140706051966808
Your birth year is approximately : 2006
(Based on your age of 17)
Note: Your height was converted from float 1.68 to integer 1 for rounding.
Thank you for using the personal data collector. Goodbye!
*/
