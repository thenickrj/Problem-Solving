class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m
        neighbors = lambda x, y: [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        @cache
        def dfs(x, y):
            return max(1 + dfs(dx, dy)
                       if inbound(dx, dy) and matrix[dx][dy] > matrix[x][y]
                       else 1
                       for dx, dy in neighbors(x, y)
                      )
        
        return max(dfs(x, y) for x, y in product(range(n), range(m)))