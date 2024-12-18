import math
import re

def solution(file, row, col):
    with open(file, "r") as f:
        lines = f.readlines()
    
    ROWS, COLS = row, col
    QROW, QCOL = row // 2, col //2

    min_res = math.inf
    lis = tuple(tuple(map(int, re.findall("-?\d+", line))) for line in lines)
    for second in range(10000):
        quad = [0, 0, 0, 0]
        second += 1
        for c, r, vc, vr in lis:
            r = (r + vr * second) % ROWS
            c = (c + vc * second) % COLS

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

        if safety_code < min_res:
            min_res = min(safety_code, min_res)
            res = second

    return res

if __name__ == "__main__":
    print( solution("day14/data.txt", 103, 101) )