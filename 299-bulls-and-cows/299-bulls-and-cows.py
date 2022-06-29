class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = Counter(secret)
        bulls,cows = 0,0
        
        
        for i,num in enumerate(guess):
            if num in freq:
                if num == secret[i]:
                    bulls+=1
                    
                    if freq[num] <= 0:
                        cows-=1
                else:
                    if freq[num] > 0:
                        cows+=1
                
                freq[num] -= 1
            
           
        return f'{bulls}A{cows}B'
            