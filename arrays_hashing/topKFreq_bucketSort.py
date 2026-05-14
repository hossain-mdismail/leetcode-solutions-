class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count the frequency of each number
        # Time: O(n)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2. Create the "Buckets" (List of Lists)
        # The index will represent the frequency. 
        # Size is len(nums) + 1 to account for index 0 and max frequency.
        freq = [[] for i in range(len(nums) + 1)]

        # 3. Fill the buckets
        # Map the number to the index that represents its frequency
        # Time: O(n)
        for num, cnt in count.items():
            freq[cnt].append(num)

        # 4. Collect the top k elements
        # Move backwards through the buckets (highest frequency first)
        # Time: O(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we have found k elements, we are done
                if len(res) == k:
                    return res