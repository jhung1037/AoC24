def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        lis = list(map(int, line.split()))
        ASC = 1 if (lis[1] - lis[0]) > 0 else -1
        res += 1
        for i in range(1, len(lis)):
            if not (1 <= (lis[i] - lis[i-1]) * ASC <= 3):
                res -= 1
                break

    return res

if __name__ == "__main__":
    assert solution("day2/test.txt") == 2
    print( solution("day2/data.txt") )
