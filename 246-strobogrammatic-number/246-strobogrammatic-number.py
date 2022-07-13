class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lookup = {
            "6" : "9",
            "9" : "6",
            "8" : "8",
            "1" : "1",
            "0" : "0"
        }
        
        convert = ""
        for ch in num:
            if ch in lookup:
                convert += lookup[ch]
            
            else:
                return False
        
        return int(convert) == int(num[::-1])
        
        
        