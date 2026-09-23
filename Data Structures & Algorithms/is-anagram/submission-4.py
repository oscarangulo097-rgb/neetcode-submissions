class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n=[0]*27
        m=[0]*27

        
        for char in s:
            print(char)
            n[ord(char.lower())-96] += 1
        for char in t:
            m[ord(char.lower())-96] += 1
        if n == m:
            return True 
    
        return False