class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_str = str(x)
        # return x_str == x_str[::-1]

        if x < 0:
            return False

        x_list = []

        while  x / 10 > 0:
            x_list.append(x % 10)
            x = x // 10
            print(x_list)
            print(x)

        return x_list == x_list[::-1]




s = Solution()
assert s.isPalindrome(121) == True
assert s.isPalindrome(-121) == False
assert s.isPalindrome(10) == False