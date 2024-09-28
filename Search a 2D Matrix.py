import math
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        arr= []
        for row in matrix:
            for x in row:
                arr.append(x)
        print(arr)
        return self.binarySearch(arr,0,len(arr)-1,target)
        
    def binarySearch(self,arr,start,end,target):
        
        mid =  math.ceil(start+(end-start)/2)
        while(start<=end):
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                return self.binarySearch(arr,mid+1,end,target)
            else:
                return self.binarySearch(arr,start,mid-1,target)

        return False
    
class Solutionn(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        size =len(matrix)*len(matrix[0])
        print(size)
        return self.binarySearch(matrix,0,size-1,target)
       
        
    def binarySearch(self,matrix,left,right,target):
        mid = left+(right-left)//2
        if(left<=right):
            col_length = len(matrix[0])
            row = int(mid/col_length)
            col= mid%col_length
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                return self.binarySearch(matrix,left,mid-1,target)
            elif matrix[row][col]<target:
                return self.binarySearch(matrix,mid+1,right,target)
        else:
            return False


s = Solutionn()
matrix = [[1],[3]]
target = 2
print(s.searchMatrix(matrix=matrix,target=target))