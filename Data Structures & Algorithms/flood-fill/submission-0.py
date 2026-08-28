class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        og = image[sr][sc]
        q.append((sr,sc))
        image[sr][sc] = color

        while q:
            r,c = q.popleft()
            if r + 1 < len(image) and image[r+1][c] != color and image[r+1][c] ==og:
                image[r+1][c] = color
                q.append((r+1,c))
            if r - 1 >=0 and image[r-1][c] != color and image[r-1][c] ==og:
                image[r-1][c] = color
                q.append((r-1,c))
            if c + 1 < len(image[0]) and image[r][c+1] != color and image[r][c+1] ==og:
                image[r][c+1] = color
                q.append((r,c+1))
            if c - 1 >=0 and image[r][c-1] != color and image[r][c-1] ==og:
                image[r][c-1] = color
                q.append((r,c-1))
        return image

            
                

