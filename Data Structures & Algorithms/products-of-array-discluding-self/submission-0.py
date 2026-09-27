class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        a = []
        mul = 1

        # Product of elements before i
        for i in range(n):
            a.append(mul)
            mul = mul * nums[i]

        # Product of elements after i
        mul = 1

        for i in range(n - 1, -1, -1):
            a[i] = a[i] * mul
            mul = mul * nums[i]

        return a