class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max = 0
        
        def bt(idx, cur_str):
            if len(cur_str) == len(set(cur_str)):
                self.max = max(len(cur_str), self.max)
            else:
                return
            
            for i in range(idx, len(arr)):
                bt(i, cur_str + arr[i])
        
        
        bt(0, "")
        return self.max