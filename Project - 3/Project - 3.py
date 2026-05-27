students = []
while True:
    print("Select an option:")
    print("Press 1 for Add Students")
    print("Press 2 for Display All Students")
    print("Press 3 for Update Student Information")
    print("Press 4 for Delete Students")
    print("Press 5 for Display Subjects Offered")
    print("Press 6 for Exit")
    print()

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            Student_ID = int(input("Enter your Student ID: "))
            Name = input("Enter your Name: ")
            Age = int(input("Enter your Age: "))
            Grade = input("Enter your Grade: ")
            Date_of_Birth = input("Enter your Date of Birth: ")
            Subjects = input("Enter your Subjects: ")

            student = {"Student ID": Student_ID, "Name": Name, "Age": Age, "Grade": Grade, "Date of Birth": Date_of_Birth, "Subjects": Subjects}
            students.append(student)
            print("Student added successfully!")
            print()
        case 2:
            if not students:
                print("No Data Found of Any Student....")
            for stu in students:
                print(f"Student ID: {stu['Student ID']} | Name: {stu['Name']} | Age: {stu['Age']} | Grade: {stu['Grade']} | Date of Birth: {stu['Date of Birth']} | Subjects: {stu['Subjects']}")
            print()
        case 3:
            Student_ID = int(input("Enter your student ID: "))
            found = False

            for stu in students:
                if stu["Student ID"] == Student_ID:
                    found = True
                    while True:
                        print("Press 1 for Update Name")
                        print("Press 2 for Update Age")
                        print("Press 3 for Update Grade")
                        print("Press 4 for Update Subjects")
                        print("Press 5 for Exit")

                        operation = int(input("Enter operation: "))
                        match operation:
                            case 1:
                                new_name = input("Enter your name: ")
                                stu['name'] = new_name
                            case 2:
                                new_age = input("Enter your age: ")
                                stu['age'] = new_age
                            case 3:
                                new_grade = input("Enter your grade: ")
                                stu['grade'] = new_grade
                            case 4:
                                new_subjects = input("Enter your subjects: ")
                                stu['subjects'] = new_subjects
                            case 5: break
                            case _: print("Invalid Operation")
                    print("Update Student Success")
            if found == False:
                print("No Record Found....")
            print()
        case 4:
            Student_ID = int(input("Enter your student ID: "))
            found = False

            for stu in students:
                if stu["Student ID"] == Student_ID:
                    found = True
                    students.remove(stu)
                    print("Delete Student Success")
            if found == False:
                print("No Record Found....")
            print()
        case 5:
            subjects_offered = [
                "Mathematics",
                "Science",
                "English",
                "Computer Studies",
                "History",
                "Accounts",
                "Statistics"
            ]
            print("Subjects Offered: ")

            for subject in subjects_offered:
                print("-", subject)
            print()
        case 6: break
        case _: print("Invalid Choice")
