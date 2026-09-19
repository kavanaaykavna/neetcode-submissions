class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = 0 
        max_sum = nums[0]
        subarray=[]
        for i in nums:
            Sum = Sum+i
            subarray.append(i)
            if(Sum>=max_sum):
                
                max_sum = Sum
            if(Sum<0):
                Sum = 0 
                subarray = []
            
        return max_sum

obj = Solution()
res = obj.maxSubArray([-1])
print(res)