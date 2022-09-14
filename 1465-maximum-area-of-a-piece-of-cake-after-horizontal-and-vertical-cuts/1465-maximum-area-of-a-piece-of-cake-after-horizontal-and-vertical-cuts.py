class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        maxHor = 0
        maxVer = 0
        for i in range(1, len(horizontalCuts)):
            maxHor = max(maxHor, horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, len(verticalCuts)):
            maxVer = max(maxVer, verticalCuts[i] - verticalCuts[i-1])
        print(maxHor, maxVer)
        return (maxHor * maxVer) % (10 ** 9 + 7)
        
    