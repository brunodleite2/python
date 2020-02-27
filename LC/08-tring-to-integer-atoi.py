class Solution:
    MAX = 2**31 -1
    MIN = 2**31 * -1

    def __is_sign(self, char: str) -> bool:
        if char in ['-','+']:
            return True
        return False

    def __is_number(self, char: str) -> bool:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        return False

    def __is_whitespace(self, char: str) -> bool:
        if char == ' ':
            return True
        return False

    def __convert_to_int(self, str: str) -> int:
        if not len(str) or (len(str) == 1 and not self.__is_number(str[0])):
            return 0

        integer = int(str)

        if integer > Solution.MAX:
            return Solution.MAX

        if integer < Solution.MIN:
            return Solution.MIN

        return integer


    def myAtoi(self, str: str) -> int:
        number_has_started = False
        response = ""

        for char in str:
            if not number_has_started:
                if self.__is_whitespace(char):
                    continue

                if self.__is_sign(char) or self.__is_number(char):
                    response += char
                    number_has_started = True
                    continue
                # Letter!!
                return 0

            # number has started
            if self.__is_number(char):
                response += char
                continue

            # number has finished
            return self.__convert_to_int(response)

        return self.__convert_to_int(response)


solution = Solution()
assert solution.myAtoi('42') == 42
assert solution.myAtoi('  -42') == -42
assert solution.myAtoi('words and 987') == 0
assert solution.myAtoi('-91283472332') == -2147483648