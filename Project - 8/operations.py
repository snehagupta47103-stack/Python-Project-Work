import numpy as np
from arrays import ArrayOperations


class Operations(ArrayOperations):

    def addition(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nEnter Value to Add : "))

        print("\nResult")
        print(self.array + value)

    def subtraction(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nEnter Value to Subtract : "))

        print("\nResult")
        print(self.array - value)

    def multiplication(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nEnter Value to Multiply : "))

        print("\nResult")
        print(self.array * value)

    def division(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nEnter Value to Divide : "))

        if value == 0:
            print("\nDivision by zero is not allowed.")
            return

        print("\nResult")
        print(self.array / value)

    def dot_product(self):

        if self.array is None or self.array.ndim != 1:
            print("\nCreate a 1D Array First.")
            return

        print("\nEnter Second Array")

        data = []

        for i in range(len(self.array)):
            data.append(int(input(f"Element {i+1} : ")))

        second = np.array(data)

        print("\nDot Product :", np.dot(self.array, second))

    def matrix_multiplication(self):

        if self.array is None or self.array.ndim != 2:
            print("\nCreate a 2D Array First.")
            return

        rows, cols = self.array.shape

        print("\nEnter Second Matrix")

        matrix = []

        for i in range(rows):

            row = []

            for j in range(cols):

                row.append(int(input(f"Element[{i}][{j}] : ")))

            matrix.append(row)

        second = np.array(matrix)

        print("\nMatrix Multiplication")
        print(np.matmul(self.array, second))

    def combine_arrays(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        print("\nEnter Second Array")

        data = []

        for i in range(self.array.size):
            data.append(int(input(f"Element {i+1} : ")))

        second = np.array(data).reshape(self.array.shape)

        print("\n1. Horizontal Combine")
        print("2. Vertical Combine")

        choice = int(input("\nEnter Choice : "))

        if choice == 1:
            print(np.hstack((self.array, second)))

        elif choice == 2:
            print(np.vstack((self.array, second)))

        else:
            print("\nInvalid Choice.")

    def split_array(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        parts = int(input("\nEnter Number of Parts : "))

        result = np.array_split(self.array, parts)

        print()

        for i, part in enumerate(result, start=1):
            print(f"Part {i}")
            print(part)