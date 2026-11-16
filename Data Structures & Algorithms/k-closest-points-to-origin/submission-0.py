import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.dis = []
        self.point = []
        for i, lst in enumerate(points):
            d = math.sqrt((0-lst[0])**2 + (0-lst[1])**2)
            tup = [d,i]
            self.dis.append(tup)
        
        self.quickSort(self.dis, 0, len(points)-1)

        for i in range(k):
            res = self.dis[i][1]
            self.point.append(points[res])
        
        return self.point


    
    def quickSort(self, arr, s, e):
        if e-s+1 <= 1:
            return arr
        
        pivot = arr[e][0]
        left = s

        for i in range(s, e):
            if arr[i][0] <= pivot:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        temp = arr[left]
        arr[left] = arr[e]
        arr[e] = temp

        self.quickSort(arr, s, left-1)
        self.quickSort(arr, left+1, e)

        return arr