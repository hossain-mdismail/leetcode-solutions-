from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list) #[['a','c','t'] : 'cat',..], but list can not be a key- will make it tuple
        for word in strs:
            sorted_w = tuple(sorted(word)) # sorted gives a list ['a','c','t'], 
                                    # list can not be a key, so make it tuple
            sorted_dict[sorted_w].append(word) # that means anagram exists, put them together
            
        return list(sorted_dict.values())






'''
- get each 'word' from the -> 'strs' list 
-    count each 'letter' of this word, put the 'letter_count'  in a dict {}
- 
-
'''        