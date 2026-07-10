import numpy as np

class DataAnalytics:
    object_count = 0

    def __init__(self):
        self.array = None
        DataAnalytics.object_count += 1

    def __display_array(self):

        if self.array is None:
            print("\nNo Array Created.")
        else:
            print("\nCurrent Array")
            print(self.array)

    def display_array(self):

        self.__display_array()

    def array_information(self):

        if self.array is None:
            print("\nNo Array Created.")
            return

        print("\n========== ARRAY INFORMATION ==========")
        print("Array :", self.array)
        print("Shape :", self.array.shape)
        print("Dimension :", self.array.ndim)
        print("Size :", self.array.size)
        print("Data Type :", self.array.dtype)

    @classmethod
    def total_objects(cls):

        print("\nTotal Objects Created :", cls.object_count)

    @staticmethod
    def project_information():

        print("\n========== PROJECT DETAILS ==========")
        print("Project Name : NumPy Analyzer")
        print("Language     : Python")
        print("Library      : NumPy")