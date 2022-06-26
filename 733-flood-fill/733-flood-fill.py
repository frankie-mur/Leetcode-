class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0]) 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        new_color = image[sr][sc]
        if new_color == color:
            return image
        
        def dfs(image, sr, sc, color, new_color):
            nonlocal R
            nonlocal C
            nonlocal directions   
            if (sr < 0 or sc < 0 or sr >= R or sc >= C or image[sr][sc] != color):
                return
            
            image[sr][sc] = new_color
            for x,y in directions:
                dfs(image, sr + x, sc + y, color, new_color)
        
        
        dfs(image,sr,sc,new_color,color)
        return image
        
        