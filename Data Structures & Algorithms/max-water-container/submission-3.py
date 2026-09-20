class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:

            h = min(heights[left], heights[right])
            width = right - left
            area = h * width

            if area > max_area:
                max_area = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

obj = Solution()
res = obj.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6])
print(res)
            