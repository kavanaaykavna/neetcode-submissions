class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = []
        for row in grid:
            for element in row:
                if element in seen:
                    a.append(element)
                else:
                    seen.add(element)
        for i in range(1, len(grid)**2 + 1):
             if i not in seen:
                a.append(i)
        return a 
obj = Solution()
res = obj.findMissingAndRepeatedValues([[1,3],[2,2]])
print(res)
        


