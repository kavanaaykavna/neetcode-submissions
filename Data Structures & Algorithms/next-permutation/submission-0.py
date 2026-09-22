class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the pivot
        i = n - 2

        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        # Step 2: If pivot exists, find the number to swap with it
        if i >= 0:
            j = n - 1

            while j > i:
                if nums[j] > nums[i]:
                    break
                j -= 1

            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse everything after i
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1