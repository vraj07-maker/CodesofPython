class Solution:

  def reverseDegree(self, s: str) -> int:
    mapping = {
        'a': 26,
        'b': 25,
        'c': 24,
        'd': 23,
        'e': 22,
        'f': 21,
        'g': 20,
        'h': 19,
        'i': 18,
        'j': 17,
        'k': 16,
        'l': 15,
        'm': 14,
        'n': 13,
        'o': 12,
        'p': 11,
        'q': 10,
        'r': 9,
        's': 8,
        't': 7,
        'u': 6,
        'v': 5,
        'w': 4,
        'x': 3,
        'y': 2,
        'z': 1,
    }

    total_score = 0
    index = 1  # <--- DEFINE THIS BEFORE THE LOOP

    for char in s:
      if char in mapping:
        total_score += mapping[char] *index
        index += 1  # Increment for the next character

    return total_score


# Local runner
sol = Solution()
print(sol.reverseDegree("abc"))  # Output: 148