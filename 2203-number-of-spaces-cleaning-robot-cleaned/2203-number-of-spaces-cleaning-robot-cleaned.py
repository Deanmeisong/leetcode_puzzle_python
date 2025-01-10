class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        def dfs(i,j,k):
            if (i,j,k) in vis: return
            vis.add((i,j,k))
            nonlocal ans
            ans += room[i][j] == 0
            room[i][j] = -1
            x, y = i+dirs[k], j+dirs[k+1]
            if 0<=x<len(room) and 0<=y<len(room[0]) and room[x][y] != 1:
                dfs(x,y,k)
            else:
                dfs(i,j,(k+1)%4)
        
        ans = 0
        vis = set()
        dirs = (0,1,0,-1,0)
        dfs(0,0,0)
        return ans
       
