class TimeMap:
    def __init__(self):
        self.key_time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:    
        # Store '(timestamp, value)' pair in 'key' array
        self.key_time_map[key].append((timestamp, value)) 
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time_map:
            return ""
        
        return self.bns(self.key_time_map[key], timestamp)
    
    
    def bns(self, arr, target):
        left = 0
        right = len(arr) 
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid][0] <= target:
                left = mid + 1
            else:
                right = mid
        
        return "" if right == 0 else arr[right-1][1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)