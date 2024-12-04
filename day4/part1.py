WORD = ("X", "M", "A", "S")
DIRECTIONS = (-1, 0, 1)

def valid_count(r, c, grid):
    count = 0
    for dr in DIRECTIONS:
        for dc in DIRECTIONS:
            if ((dr, dc) != (0, 0) and 
                0 <= (r+dr*3) < len(grid) and 
                0 <= (c+dc*3) < len(grid[0]) and
                all(grid[r+dr*i][c+dc*i] == WORD[i] for i in range(1, 4))):
                count += 1
    return count
    
def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    grid = [line.strip() for line in lines]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == WORD[0]:
                res += valid_count(row, col, grid)
    
    return res

if __name__ == "__main__":
    assert solution("day4/test.txt") == 18
    print( solution("day4/data.txt") )
