class Solution:
	def maxLength(self, arr):
		self.maximum = 0

		def backtrack(start,s):
			if len(s)==len(set(s)):
				self.maximum = max(self.maximum,len(s))
			else:
				return
			for i in range(start,len(arr)):
				backtrack(i+1,s + arr[i])

		backtrack(0,"")
		return self.maximum
                    
                        
                    
                    
                
                    
                
            