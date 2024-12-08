def foward(r, c, dr, dc, lab):
    if not (0 <= r+dr < len(lab) and 0 <= c+dc < len(lab[0])):
        return (-1, -1, 0, 0)
    if lab[r+dr][c+dc] == "#":
        dr, dc = dc, -dr
    return (r+dr, c+dc, dr, dc)

def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    lab = []
    start_pos = None
    for row, line in enumerate(lines):
        if start_pos is None and "^" in line:
            start_pos = (row, line.index("^"))
        lab.append(line)

    r, c = start_pos
    dr, dc = -1, 0
    visited = set()
    while r >= 0 and c >= 0:
        visited.add((r, c))
        r, c, dr, dc = foward(r, c, dr, dc, lab)

    return len(visited)

if __name__ == "__main__":
    assert solution("day6/test.txt") == 41
    print( solution("day6/data.txt") )
