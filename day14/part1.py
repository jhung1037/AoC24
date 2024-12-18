import re

def solution(file, row, col):
    with open(file, "r") as f:
        lines = f.readlines()
    
    ROWS, COLS = row, col
    QROW, QCOL = row // 2, col //2
    quad = [0] * 4

    for line in lines:
        c, r, vc, vr = tuple(map(int, re.findall("-?\d+", line)))
        r = (r + vr * 100) % ROWS
        c = (c + vc * 100) % COLS

        if r < QROW and c < QCOL:
            quad[0] += 1
        elif r < QROW and c > QCOL:
            quad[1] += 1
        elif r > QROW and c < QCOL:
            quad[2] += 1
        elif r > QROW and c > QCOL:
            quad[3] += 1

    safety_code = 1
    for num in quad:
        safety_code *= num
    return safety_code

if __name__ == "__main__":
    assert solution("day14/test.txt", 7, 11) == 12
    print( solution("day14/data.txt", 103, 101) )
