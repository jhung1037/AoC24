import re

def mul(a, b):
    return a * b

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    enabled = True
    for line in lines:
        matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            else:
                res += eval(match) if enabled else 0

    return res

if __name__ == "__main__":
    assert solution("day3/test.txt") == 48
    print( solution("day3/data.txt") )
