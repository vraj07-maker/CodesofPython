class Solution:

  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]

      if current_sum == target:
        # 1-indexed as requested by the problem
        return [left + 1, right + 1]
      elif current_sum > target:
        # Sum is too big, move right pointer inward to lower the sum
        right -= 1
      else:
        # Sum is too small, move left pointer inward to raise the sum
        left += 1