class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        U-Given a string s and an string p find all anagrams of p in s, return the starting indices of all these anagrams
        M- Two pointer, with hashmap to ensure anagram
        P- while w_end has not reached end of s
                -if the rch is in the pfreq map than subtract its value by one
                    -if the value reaches zero than count for a lost word
                -if the count is equal to the length of p than we have an anagram
                    -append w_start to res
                -if the window size is greater then the size of p than it cannot be and anagram, therefore check if window start is in pfreq
                    -if its value is zero than decrement count
                -incremnet its value by one
            -increment w_end
                
        I- Python

        R-Pretty tough solution, need to review sliding window theory. Although I was very close needed a little hint to get me there.

        E- Time: O(n) loop through both s and p 
           Space: O(n) dict map 

        '''
        pfreq, res, w_start,w_end, wordl = Counter(p), [], 0,0,0
        while w_end < len(s):
            rch = s[w_end]
            if rch in pfreq:
                pfreq[rch] -= 1
                if pfreq[rch] == 0:
                    wordl += 1
            if wordl == len(pfreq):
                res.append(w_start)
            if w_end - w_start >= len(p) - 1:
                lch = s[w_start]
                if lch in pfreq:
                    if pfreq[lch] == 0:
                        wordl -= 1
                    pfreq[lch] += 1
                w_start += 1
            w_end += 1
        
        return res
            
                
        
        