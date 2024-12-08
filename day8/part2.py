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
                dr, dc = ar-br, ac-bc
                
                r, c = br, bc
                while in_grid(r,c):
                    antinodes.add((r, c))
                    r, c = r+dr, c+dc

                r, c = ar, ac
                while in_grid(r,c):
                    antinodes.add((r, c))
                    r, c = r-dr, c-dc

    return len(antinodes)

if __name__ == "__main__":
    assert solution("day8/test.txt") == 34
    print( solution("day8/data.txt") )
