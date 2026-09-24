class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        arr = [0]*27
        balloon = 0
        for char in text:
            arr[ord(char.lower())-97] += 1 
        
        print(arr)
        while arr[1] >= 1 and arr[0] >= 1 and arr[11] >= 2 and arr[14] >= 2 and arr[13] >=1:
            print("inside")
            arr[1] -=1
            arr[0]-=1
            arr[11]-=2
            arr[14]-=2
            arr[13]-=1
            print(arr)
            balloon +=1

        return balloon