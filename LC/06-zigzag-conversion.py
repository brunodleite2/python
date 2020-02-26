class Solution:
    DIRECTION_DOWN = 1
    DIRECTION_UP = -1

    def __init__(self):
        self.direction = Solution.DIRECTION_DOWN

    def reverse_direction(self):
        if self.direction == Solution.DIRECTION_DOWN:
            self.direction = Solution.DIRECTION_UP
            return

        self.direction = Solution.DIRECTION_DOWN

    def initialize_result_dict(self, numRows: int) -> dict:
        result_dict = {}  # Row Number : List
        for row_number in range(numRows):
            result_dict[row_number] = ""

        return result_dict

    def get_result_str(self, result_dict: dict,  numRows: int) -> dict:
        result_str = ""
        for row_number in range(numRows):
            result_str += result_dict[row_number]

        return result_str

    def convert(self, s: str, numRows: int) -> str:
        if not numRows:  # 0
            return ""

        if numRows == 1:
            return s

        self.direction = Solution.DIRECTION_DOWN
        result_dict = self.initialize_result_dict(numRows)
        row_number = 0

        for char in s:
            result_dict[row_number]+=char

            row_number += self.direction

            if row_number == numRows:
                self.reverse_direction()
                row_number -= 2

            if row_number == 0:
                self.reverse_direction()

        return self.get_result_str(result_dict, numRows)

