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
                
'''
        If everyone in freq[i] belongs in the result, why not just grab the whole list at once?
--> The reason we use a second loop to append items one by one is because of the value of k
freq[2] = [1, 2, 3] (All three numbers appeared twice).
If you did res.extend(freq[2]) or res += freq[2], your result would be [1, 2, 3]
Problem: You now have 3 elements, but the user only asked for k=2.
  
  
  Efficiency:
                If k is 10, but the highest frequency bucket freq[100] has 500 numbers in it, appending the "whole list" would waste time and memory by grabbing 490 numbers you don't need. The for loop ensures we only take what we need and immediately exit the entire function.
'''
                