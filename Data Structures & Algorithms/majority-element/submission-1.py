
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Max = 0
        e = 0
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

            if frequency[num] > Max:
                Max = frequency[num]
                e = num

        return e


obj = Solution()
res = obj.majorityElement([5, 5, 1, 1, 1, 5, 5])
print(res)

