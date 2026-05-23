print("Welcome to the Pattern generator and number analyzer")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze Number")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        rows_in = input("enter the number of rows for the Pattern:")
        if not rows_in.isdigit():
            print("Error: Please enter a positive integer.")
            continue

        rows = int(rows_in)
        if rows <= 0:
            print("Error: Number of rows must be greater than 0")
            break

        print("Pattern:")
        i = 1
        while i <= rows:
            for j in range(1, i + 1):
                print("*",end=" ")
            print()
            i += 1


    elif choice == '2':
         start_in = input("Enter start of range: ")
         end_in = input("Enter end of range: ")

         try:
             start = int(start_in)
             end = int(end_in)
         except ValueError:
             print("Error: Enter valid integers.")
             continue

         if end < start:
             print("Error: End must be >= Start.")
             continue

         total_sum = 0
         for num in range(start,end + 1):
             if num == 0:
                 pass
             if num % 2 == 0:
                 print(f"Number {num} is Even")
             else:
                 print(f"Number {num} is Odd")
             total_sum += num
             print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

    elif choice == '3':
          print("Thank you for using the program! Goodbye!")
          break
    else:
          print("Invalid choice! Try again.")
         
