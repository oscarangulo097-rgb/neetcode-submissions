class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max = 0
        while  r > l:
            area = (r-l)*min(heights[l],heights[r])
            if area > max:
                max = area
                continue
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return max 
