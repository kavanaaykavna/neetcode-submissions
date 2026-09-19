class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b=[]
        for i in range(0,n):
            for j in range(i+1, n ):
                if(prices[i]<prices[j]):
                    a = (prices[j]-prices[i])
                    b.append(a)

        if len(b)==0:
            return 0 
        return max(b)
obj = Solution()
res = obj.maxProfit([10,1,5,6,7,1])
print(res)