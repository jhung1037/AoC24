import re

def mul(a, b):
    return a * b

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        matches = re.findall("mul\(\d+,\d+\)", line)
        for match in matches:
            res += eval(match)

    return res

if __name__ == "__main__":
    assert solution("day3/test.txt") == 161
    print( solution("day3/data.txt") )
