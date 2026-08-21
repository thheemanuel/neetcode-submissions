class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = 0
        fresh_oranges = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and fresh_oranges > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh_oranges -= 1
            time += 1
        
        if fresh_oranges == 0:
            return time
        else:
            return -1