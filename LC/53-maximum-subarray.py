class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = 0
        max_sum = float('-inf')

        for index in range(len(nums)):
            num = nums[index]
            curr_sum += num
            max_sum = max(curr_sum, max_sum)

            next_num = 0
            if (index != len(nums) - 1):
                next_num = nums[index + 1]


            if curr_sum < 0 and next_num >= curr_sum:
                curr_sum = 0
                continue


        return max_sum
