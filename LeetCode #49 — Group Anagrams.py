from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for word in strs:
      # C-optimized Timsort makes this lightning fast
      sorted_word = "".join(sorted(word))
      res[sorted_word].append(word)

    return list(res.values())