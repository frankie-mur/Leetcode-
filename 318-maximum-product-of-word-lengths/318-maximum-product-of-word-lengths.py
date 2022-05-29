class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        nested loop throguh every word combination
        turn into set and check the union is empty (no same ch's)
        compute the max product
        '''
        prod = 0
        for i in range(len(words)):    #O(N)
            for j in range(i+1, len(words)): #O(N)
                if set(words[i]) & set(words[j]) == set(): #O(N)
                    prod = max(prod, len(words[i]) * len(words[j])) #O(1)
                                        
            
        
        return prod
                
        
       