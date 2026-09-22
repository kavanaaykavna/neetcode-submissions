class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1 , n):
                for k in range(j+1 , n):
                    for l in range(k+1 , n):
                        if(nums[i]+ nums[j]+nums[k]+nums[l]==target):
                            a = [nums[i], nums[j],nums[k],nums[l]]
                            a.sort()
                            if a not in res:
                                res.append(a)
        return res 