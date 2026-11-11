class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            m = (l+r) // 2
            left = nums[l]
            mid = nums[m]
            right = nums[r]

            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m 
        return -1 