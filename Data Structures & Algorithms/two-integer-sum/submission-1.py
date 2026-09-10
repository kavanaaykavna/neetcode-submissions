class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
                    

        return l


obj = Solution()
res = obj.twoSum([3, 4, 5, 6], 7)
print(res)