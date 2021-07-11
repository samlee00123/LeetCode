class Solution:
    def MidMaxSubArray(self, nums: List[int]) -> int:
        mid = len(nums)//2
        
        s = 0
        lefts = float('-inf')
        
        for i in range(mid, -1, -1):
            s += nums[i]

            if (s > lefts):
                lefts = s

        s = 0
        rights = float('-inf')
        
        for i in range(mid+1, len(nums)):
            s = s + nums[i]

            if (s > rights):
                rights = s
        
        return max(lefts + rights, lefts, rights)
    
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0] + nums[1], nums[0], nums[1])
        
        left = self.maxSubArray(nums[:len(nums)//2])
        right = self.maxSubArray(nums[len(nums)//2:])
        mid = self.MidMaxSubArray(nums)

        return max(left, right, mid)

            
            
            
        