class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1 , n):
                if(nums[i]>nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums[i]

obj = Solution()
res = obj.sortColors([1,0,1,2])
print(res)