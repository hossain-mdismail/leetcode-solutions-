# thhis is another fast and easy solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Guard Clause: If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # 2. Use a hash map to track character frequencies
        count = {}
        
        # 3. Increment for string 's', decrement for string 't'
        for i in range(len(s)):
            # Update count for s[i]
            count[s[i]] = count.get(s[i], 0) + 1
            # Update count for t[i]
            count[t[i]] = count.get(t[i], 0) - 1
            
        # 4. If all counts are zero, it's a perfect anagram
        for val in count.values():
            if val != 0:
                return False
                
        return True

# Time Complexity: O(n) - where n is the length of the string
# Space Complexity: O(1) - if we consider the fixed size of the alphabet

'''
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s) # look like: ['a','b','c',...]
        sorted_t = sorted(t) # ['','','',...]

        s_count = defaultdict() # it is a blank dictionary as {'letter'->str : count->int}
        t_count = defaultdict() # it is a balnk dictionary as {'letter' : count}
        

        for i in sorted_s:
            if i in s_count: # this line is possible , only because s_count is a dictionary, and i is considered as the key of that dictionary
                s_count[i]+= 1   # adding 1 to that value in s_count dictionary
            else: s_count[i]= 1

        
        for j in sorted_t:
            if j in t_count:
                t_count[j]+=1
            else: t_count[j]=1

        return s_count == t_count


        
        if len(s) != len(t):
            return false
        
        return sorted(s)==sorted(t) # sorted always returns a list of separate letters. Output: ['a', 'c', 't'] 
        '''