from analytics import Analytics
import menu


def main():

    obj = Analytics()

    while True:

        menu.main_menu()

        try:
            choice = int(input("\nEnter Your Choice : "))
        except ValueError:
            print("\nInvalid Input!")
            continue

        if choice == 1:

            while True:

                menu.array_menu()

                ch = int(input("\nEnter Choice : "))

                if ch == 1:
                    obj.create_1d_array()

                elif ch == 2:
                    obj.create_2d_array()

                elif ch == 3:
                    obj.create_3d_array()

                elif ch == 4:
                    obj.display_array()

                elif ch == 5:
                    obj.array_information()

                elif ch == 6:
                    obj.indexing()

                elif ch == 7:
                    obj.slicing()

                elif ch == 8:
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == 2:

            while True:

                menu.math_menu()

                ch = int(input("\nEnter Choice : "))

                if ch == 1:
                    obj.addition()

                elif ch == 2:
                    obj.subtraction()

                elif ch == 3:
                    obj.multiplication()

                elif ch == 4:
                    obj.division()

                elif ch == 5:
                    obj.dot_product()

                elif ch == 6:
                    obj.matrix_multiplication()

                elif ch == 7:
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == 3:

            while True:

                menu.combine_menu()

                ch = int(input("\nEnter Choice : "))

                if ch == 1:
                    obj.combine_arrays()

                elif ch == 2:
                    obj.split_array()

                elif ch == 3:
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == 4:

            while True:

                menu.analysis_menu()

                ch = int(input("\nEnter Choice : "))

                if ch == 1:
                    obj.search_element()

                elif ch == 2:
                    obj.sort_array()

                elif ch == 3:
                    obj.filter_array()

                elif ch == 4:
                    break

                else:
                    print("\nInvalid Choice!")

        elif choice == 5:

            obj.aggregate_functions()
            obj.statistics()

        elif choice == 6:

            obj.project_information()
            obj.total_objects()

        elif choice == 7:

            print("\nThank You!")
            break

        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()