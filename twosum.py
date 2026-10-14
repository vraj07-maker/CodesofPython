class Solution:

    def twosum(self, number: list[int], target: int) -> list[int]:
        left = 0
        right = len(number) - 1

        while left < right:
            current_sum = number[left] + number[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []


# Testing locally:
number = [2, 7, 9, 11, 15]
target = 9

sol = Solution()
print(sol.twosum(number, target)) 