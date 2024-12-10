NUM = tuple(str(i) for i in range(10))
DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))

def dfs(r, c, grid, i):
    if not(0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != NUM[i]:
        return 0

    if i == 9 and grid[r][c] == "9":
        return 1

    return sum(dfs(r+dr, c+dc, grid, i+1) for dr, dc in DIRECTIONS)

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    
    return sum(dfs(r, c, grid, 0) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "0")


if __name__ == "__main__":
    assert solution("day10/test.txt") == 81
    print( solution("day10/data.txt") )