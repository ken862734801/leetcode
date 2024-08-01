from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        num = 0

        def bfs(r, c):
            queue = deque()
            seen.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0. -1]]

                for dr, dc in directions:
                    r, c = r + dr, c + dc
                    if (r in range(row) and
                        c in range(col) and
                        grid[r][c] == "1" and
                        (r, c) not in seen):
                        queue.append((r, c))
                        seen.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    num += 1
        return num