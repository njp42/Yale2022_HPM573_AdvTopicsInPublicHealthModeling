
import math

class SumRatio:
    def __init__(self, x, y):
        """
        :param x: (list) of numbers
        :param y: (list) of numbers
        """
        self.x = x
        self.y = y

    def get_sum_ratio(self):
        """
        :return: x_1/y_1 + x_2+y_2 + ...
        """

        # number of ratios to calculate
        num_of_elements = len(self.x)
        assert len(self.x) == len(self.y), "x and y should have the same number of elements."

        # sum all ratios
        sum = 0.0
        for i in range(0, num_of_elements):
            try:
                sum += self.x[i]/self.y[i]

            except ZeroDivisionError:
                print("Warning: Division by zero occurred in calculating the ratio in position " + str(i) + ".")
                sum = math.nan

        return sum
