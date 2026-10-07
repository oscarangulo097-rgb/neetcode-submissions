class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        mid = n // 2

        if n ==1 or n ==0:
            return nums


        arr1 = nums[:mid].copy()
        arr2 = nums[mid:].copy()

        arr1 = self.sortArray(arr1)
        arr2 = self.sortArray(arr2)

        res = self.mergeSort(arr1,arr2)

        return res 

    def mergeSort(self,arr1, arr2):
        i,j = 0,0
        res = []
        while i < len(arr1) and j < len(arr2):
            elem1 = arr1[i]
            elem2 = arr2[j]
            
            if elem1 < elem2:
                res.append(elem1)
                i+=1
            else:
                res.append(elem2)
                j+=1

        while i < len(arr1):
            elem = arr1[i]
            res.append(elem)
            i+=1

        while j < len(arr2):
            elem = arr2[j]
            res.append(elem)
            j += 1
        return res