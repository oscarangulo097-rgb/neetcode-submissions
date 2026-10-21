class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            dp[num] = i
        
        for i in range(n):
            num = nums[i]
            need = target - num 

            if need in dp:
                j = dp[need]
                if i != j:
                    return[i,j]
            