from collections import defaultdict

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    a, b = defaultdict(int), defaultdict(int)
    for line in lines:
        x, y = map(int, line.split())
        a[x] += 1
        b[y] += 1

    res = 0 
    for num, count in a.items():
        res += num * count * b[num]

    return res

if __name__ == "__main__":
    assert solution("day1/test.txt") == 31
    print( solution("day1/data.txt") )
