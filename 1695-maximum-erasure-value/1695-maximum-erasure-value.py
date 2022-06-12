class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        mxscore = 0
        N = len(nums)
        wstart = 0
        curscore = 0
        wend = 0
        while wend < N:
            rnum = nums[wend]
            if rnum not in seen:
                curscore += rnum
                mxscore = max(mxscore, curscore)
                seen.add(rnum)
                wend+=1
            else:
                lnum = nums[wstart]
                if lnum in seen:
                    seen.remove(lnum)
                wstart+=1
                curscore -= lnum
    
            
        return mxscore
        