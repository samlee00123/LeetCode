class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] > nums[j-1]:
                if j - i > length:
                    length = j - i
            else:
                i = j

        return length + 1
