import numpy as np
from operations import Operations


class Analytics(Operations):

    def search_element(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nEnter Element to Search : "))

        result = np.where(self.array == value)

        if len(result[0]) == 0:
            print("\nElement Not Found.")
        else:
            print("\nElement Found At Index :", result)

    def sort_array(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        print("\nSorted Array")
        print(np.sort(self.array))

    def filter_array(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        value = int(input("\nShow Elements Greater Than : "))

        result = self.array[self.array > value]

        print("\nFiltered Array")
        print(result)

    def aggregate_functions(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        print("\n========== AGGREGATE FUNCTIONS ==========")
        print("Sum      :", np.sum(self.array))
        print("Mean     :", np.mean(self.array))
        print("Minimum  :", np.min(self.array))
        print("Maximum  :", np.max(self.array))

    def statistics(self):

        if self.array is None:
            print("\nPlease Create an Array First.")
            return

        print("\n========== STATISTICAL ANALYSIS ==========")

        print("Mean                 :", np.mean(self.array))
        print("Median               :", np.median(self.array))
        print("Minimum              :", np.min(self.array))
        print("Maximum              :", np.max(self.array))
        print("Standard Deviation   :", np.std(self.array))
        print("Variance             :", np.var(self.array))
        print("50th Percentile      :", np.percentile(self.array, 50))

        if self.array.ndim == 1 and self.array.size > 1:

            print("\nCorrelation Coefficient")

            second = self.array + 1

            print(np.corrcoef(self.array, second))