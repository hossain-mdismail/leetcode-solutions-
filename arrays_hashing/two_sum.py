# LeetCode 1: Two Sum
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # it is an empty dictionary where key is nums and value is indexes
        for i in range(len(nums)):  # i is the index of nums here
            
            diff = target - nums[i]
            if diff in seen: # diff is the key
                print(f"matched pair found")
                return [seen[diff],i]
            else: seen[nums[i]] = i # seen = {val : index}
                
    
# Local testing
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    result = sol.twoSum(nums, target)
    print("Output:", result)