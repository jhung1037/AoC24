def is_valid(lis, skip_index, ASC):
    prev = None
    for i, num in enumerate(lis):
        if i == skip_index:
            continue
        if prev is not None:
            if not (1 <= (num - prev) * ASC <= 3):
                return False
        prev = num
    return True

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
        
    res = 0
    for line in lines:
        lis = list(map(int, line.split()))
        for skip_index in range(len(lis)):
            if ((is_valid(lis, skip_index, ASC = 1)) or
                (is_valid(lis, skip_index, ASC = -1))):
                res += 1
                break

    return res

if __name__ == "__main__":
    assert solution("day2/test.txt") == 4
    print( solution("day2/data.txt") )
