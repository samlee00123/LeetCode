class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while True:
            try:
                if nums[i] == val:
                    nums.pop(i)
                    i -= 1
            except IndexError:
                break
            i += 1

        return len(nums)
