class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j= i+1
            while (j<len(nums)):
                if(nums[i]== nums[j]):
                     nums.remove(nums[j])
                else:
                     j+=1
            k = len(nums)

                    
        return k 

obj = Solution()
res = obj.removeDuplicates([1,1,2,3,4])
print(res)

