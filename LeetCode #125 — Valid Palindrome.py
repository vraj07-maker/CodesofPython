class Solution:

  def isPalindrome(self, s: str) -> bool:
    # 1. Clean the string
    cleaned = "".join([c.lower() for c in s if c.isalnum()])

    # 2. Set up initial pointers
    left = 0
    right = len(cleaned) - 1

    # 3. Two-pointer check
    while left < right:
      if cleaned[left] != cleaned[right]:
        return False  # Mismatch found, definitely not a palindrome

      # Characters match, move inward to check next pair
      left += 1
      right -= 1

    # 4. If all pairs matched, it's a valid palindrome
    return True