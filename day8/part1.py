from collections import defaultdict

def solution(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()

    dic = defaultdict(list)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != ".":
                dic[char].append((row, col))

    in_grid = lambda r, c: 0 <= r < len(lines) and 0 <= c < len(lines[0])

    antinodes = set()
    for char in dic:
        for i in range(len(dic[char])):
            for j in range(i+1, len(dic[char])):
                ar, ac = dic[char][i]
                br, bc = dic[char][j]
                
                r1, c1 = ar+(ar-br), ac+(ac-bc)
                r2, c2 = br+(br-ar), bc+(bc-ac)
                if in_grid(r1, c1):
                    antinodes.add((r1, c1))
                if in_grid(r2, c2):
                    antinodes.add((r2, c2))
                    
    return len(antinodes)

if __name__ == "__main__":
    assert solution("day8/test.txt") == 14
    print( solution("day8/data.txt") )
