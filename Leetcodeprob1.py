print("My first leetcode problem")
nums=[2,7,11,15]
target=9
class Solution:
  def twosum(self, nums: list[int], target: int) -> list[int]:
    visible = {}
    for i,num1 in enumerate(nums):
      num2 = target-num1
      if num2 in visible:
        return [visible[num2], i]
      visible[num1] = i
    return []

solution=Solution()
print(f"nums: {nums}, target: {target}")
print("answer:",solution.twosum(nums, target))