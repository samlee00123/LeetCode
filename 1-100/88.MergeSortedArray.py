class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) != m:
            del nums1[-1]

        for j in range(n):
            i = 0
            if(i != m + j):
                while nums1[i] <= nums2[j]:
                    i += 1
                    if i == m + j:
                        break
            nums1.insert(i, nums2[j])
