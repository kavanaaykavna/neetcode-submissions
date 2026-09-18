class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        result = 0

        for i in nums:
            result = result ^ i

        return result


obj = Solution()
res = obj.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(res)