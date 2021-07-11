class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            try:
                if nums[i] in nums[i+1:]:
                    nums.pop(i)
                    i -= 1
            except IndexError:
                break
            i += 1

        return len(nums)
