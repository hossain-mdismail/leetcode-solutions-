class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)    # if num key is there in count dict, take the value of it, either take 0 

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
            
        # or, we can write->>  arr = [[cnt,num] for num, cnt in count.items()]
        
        arr.sort()  # sorted based on the first element (count) ,  smallesst freq to largest -> ascending
        
        
        
        res = []
        while len(res) < k:   # i neeed top K elements,  wwhich are frequent
            res.append(arr.pop()[1]) # arr will lose it's last element
        return res
    
    
    
    '''
    Time Complexity: O(n \log n) because of the arr.sort() line.
    Space Complexity: O(n) because you stored everything in a dictionary and a list.
    '''
    