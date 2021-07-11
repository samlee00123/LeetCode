class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return min(nums)

        mid = len(nums)//2

        if nums[mid-1] > nums[mid] and nums[mid] < nums[mid+1]:
            return nums[mid]

        left = self.findMin(nums[:mid])
        right = self.findMin(nums[mid+1:])
        return min(left, right)
