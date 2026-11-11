class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        l, r = 0, n-1 

        while l <= r:
            m = (l+r) // 2

            left = nums[l]
            mid = nums[m]
            right = nums[r]

            if left <= mid <= right:
                return left
            elif left <= mid:
                l = m + 1
            elif right >= mid:
                r = m
            

