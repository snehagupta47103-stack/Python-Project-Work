import numpy as np
from data_analytics import DataAnalytics


class ArrayOperations(DataAnalytics):

    def create_1d_array(self):

        n = int(input("\nEnter Number of Elements : "))

        data = []

        for i in range(n):
            value = int(input(f"Enter Element {i + 1} : "))
            data.append(value)

        self.array = np.array(data)

        print("\n1D Array Created Successfully.")
        self.display_array()

    def create_2d_array(self):

        rows = int(input("\nEnter Number of Rows : "))
        cols = int(input("Enter Number of Columns : "))

        data = []

        print("\nEnter Elements")

        for i in range(rows):

            row = []

            for j in range(cols):

                value = int(input(f"Element[{i}][{j}] : "))
                row.append(value)

            data.append(row)

        self.array = np.array(data)

        print("\n2D Array Created Successfully.")
        self.display_array()

    def create_3d_array(self):

        depth = int(input("\nEnter Number of Matrices : "))
        rows = int(input("Enter Number of Rows : "))
        cols = int(input("Enter Number of Columns : "))

        data = []

        for d in range(depth):

            print(f"\nMatrix {d + 1}")

            matrix = []

            for i in range(rows):

                row = []

                for j in range(cols):

                    value = int(input(f"Element[{d}][{i}][{j}] : "))
                    row.append(value)

                matrix.append(row)

            data.append(matrix)

        self.array = np.array(data)

        print("\n3D Array Created Successfully.")
        self.display_array()

    def indexing(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        try:

            if self.array.ndim == 1:

                index = int(input("\nEnter Index : "))
                print("Element :", self.array[index])

            elif self.array.ndim == 2:

                row = int(input("\nEnter Row : "))
                col = int(input("Enter Column : "))

                print("Element :", self.array[row, col])

            elif self.array.ndim == 3:

                matrix = int(input("\nEnter Matrix : "))
                row = int(input("Enter Row : "))
                col = int(input("Enter Column : "))

                print("Element :", self.array[matrix, row, col])

        except IndexError:

            print("\nInvalid Index!")

    def slicing(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        try:

            if self.array.ndim == 1:

                start = int(input("\nEnter Start Index : "))
                end = int(input("Enter End Index : "))

                print("\nSliced Array")
                print(self.array[start:end])

            elif self.array.ndim == 2:

                rs = int(input("\nRow Start : "))
                re = int(input("Row End : "))
                cs = int(input("Column Start : "))
                ce = int(input("Column End : "))

                print("\nSliced Array")
                print(self.array[rs:re, cs:ce])

            elif self.array.ndim == 3:

                m = int(input("\nMatrix Number : "))
                rs = int(input("Row Start : "))
                re = int(input("Row End : "))
                cs = int(input("Column Start : "))
                ce = int(input("Column End : "))

                print("\nSliced Array")
                print(self.array[m, rs:re, cs:ce])

        except:

            print("\nInvalid Input.")