nums=[1,2,3,5,1]
class Solution:

  def dupsNum(self, nums):
    seen = set()

    for num in nums:
      if num in seen:
        return True
      seen.add(num)  # Now runs on every step!

    return False

solv=Solution()
print(f"nums={nums}", "has duplicates:",solv.dupsNum(nums))
  