class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        ans = [0,0]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if (nums[i] + nums[j]) == target:
                    ans[0] = i
                    ans[1] = j
                    return ans  
        