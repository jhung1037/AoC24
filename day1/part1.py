def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    a, b = [], []
    for line in lines:
        x, y = map(int, line.split())
        a.append(x)
        b.append(y)

    a.sort()
    b.sort()
    res = 0
    for x, y in zip(a, b):
        res += abs(x-y)

    return res

if __name__ == "__main__":
    assert solution("day1/test.txt") == 11
    print( solution("day1/data.txt") )
