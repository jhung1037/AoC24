def foward(r, c, dr, dc, lab):
    if not (0 <= r+dr < len(lab) and 0 <= c+dc < len(lab[0])):
        return (-1, -1, 0, 0)
    if lab[r+dr][c+dc] == "#":
        return (r, c, dc, -dr)
    return (r+dr, c+dc, dr, dc)

def loop_found(r, c, dr, dc, lab, start_pos, checked):
    ob_r, ob_c = r+dr, c+dc

    if not (0 <= ob_r < len(lab) and 0 <= ob_c < len(lab[0])):
        return False
    if lab[ob_r][ob_c] == "^" or lab[ob_r][ob_c] == "#" or (ob_r, ob_c) in checked:
        return False
    lab[ob_r][ob_c] = "#"
    checked.add((ob_r, ob_c))

    r, c = start_pos
    dr, dc = -1, 0
    visited = set()
    while r >= 0 and c >= 0:
        visited.add((r, c, dr, dc))
        r, c, dr, dc = foward(r, c, dr, dc, lab)
        if (r, c, dr, dc) in visited:

            lab[ob_r][ob_c] = "."
            return True
    lab[ob_r][ob_c] = "."
    return False

def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    lab = []
    start_pos = None
    for row, line in enumerate(lines):
        row_lis = []
        for col, char in enumerate(line):
            if start_pos is None and char == "^":
                start_pos = (row, col)
            row_lis.append(char)
        lab.append(row_lis)

    res = 0
    r, c = start_pos
    dr, dc = -1, 0
    checked = set()
    while r >= 0 and c >= 0:
        if loop_found(r, c, dr, dc, lab, start_pos, checked):
            res += 1
        r, c, dr, dc = foward(r, c, dr, dc, lab)
    
    return res

if __name__ == "__main__":
    assert solution("day6/test.txt") == 6
    print( solution("day6/data.txt") )
