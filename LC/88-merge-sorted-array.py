class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index_nums1 = index_nums2 = 0
        used_nums1 = 0

        while index_nums2 < len(nums2):
            num2 = nums2[index_nums2]
            num1 = nums1[index_nums1]

            if num2 < num1 or used_nums1 == m:
                nums1.insert(index_nums1, num2)
                nums1.pop(len(nums1) - 1)

                index_nums1 += 1
                index_nums2 += 1
                continue
            index_nums1 += 1
            used_nums1 += 1
