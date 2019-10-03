class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        d = {}
        new_arr = []
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for k in d.values():
            if k in new_arr:
                return False
            new_arr.append(k)
        return True
                