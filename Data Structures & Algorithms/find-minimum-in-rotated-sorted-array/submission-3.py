class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            m=(l+r)//2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            elif nums[l] <= nums[m]:
                l = m+1
            elif nums[m] <= nums[r]:
                r = m
            