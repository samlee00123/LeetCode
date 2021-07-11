class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = nums[0]

        left = []
        mid = []
        right = []

        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)

        sl = len(left)
        sm = len(mid)
        sr = len(right)

        if k <= sr:
            return self.findKthLargest(right, k)
        elif sr < k and k <= sr + sm:
            return mid[0]
        else:
            return self.findKthLargest(left, k - sm - sr)
