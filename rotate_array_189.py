class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # Helper function to reverse array in-place with O(1) space
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n - k elements
        reverse(k, n - 1)