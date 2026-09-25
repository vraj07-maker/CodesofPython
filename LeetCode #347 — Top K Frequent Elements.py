class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count element frequencies manually with a standard dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Initialize bucket array (index represents frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Map numbers into buckets based on their frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Traverse buckets backwards (highest frequency to lowest)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res