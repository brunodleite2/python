class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen_nums = [] # to find loops

        while n not in seen_nums:
            seen_nums.append(n)
            nums = list(str(n))
            n = 0
            for num in nums:
                n += int(num)**2

            if n == 1:
                return True


        return Falsee