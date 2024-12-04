CHAR = ("M", "S")
DIRECTIONS = (-1, 1)

def is_shape_X(r, c, grid):
    if any(grid[r+rd][c+cd] not in CHAR for cd in DIRECTIONS for rd in DIRECTIONS):
        return False
    
    if (grid[r-1][c-1] != grid[r+1][c+1] and 
        grid[r-1][c+1] != grid[r+1][c-1]):
        return True
    
    return False
    
def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    grid = [line.strip() for line in lines]
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if grid[row][col] == "A" and is_shape_X(row, col, grid):
                res += 1
    
    return res

if __name__ == "__main__":
    assert solution("day4/test.txt") == 9
    print( solution("day4/data.txt") )
