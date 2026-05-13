from collections import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        dir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        deq = deque()
        n = len(grid)

        visit = [[0]*n for _ in range(n)]   # ✅ 독립적인 행


        if grid[0][0]:
            return -1
        deq.append([0,0,1])
        visit[0][0]=1

        while deq:
            cur = deq.popleft()
            if cur[:2] == [n-1, n-1]:
                return cur[2]

            for d in dir:
                dr = cur[0]+d[0]
                dc = cur[1]+d[1]

                if dr < 0 or dr >= n or dc < 0 or dc >= n or visit[dr][dc] or grid[dr][dc]:
                    continue
                
                visit[dr][dc]=1
                deq.append([dr,dc,cur[2]+1])

        return -1        




        
        