def get_direction(lis):
    ASC_count = DESC_count = EQUAL_count = 0
    for i in range(1, 5):
        if lis[i-1] < lis[i]:
            ASC_count += 1
        elif lis[i-1] > lis[i]:
            DESC_count += 1
        else:
            EQUAL_count += 1
    
    if EQUAL_count >= 2 or ASC_count == DESC_count: return 0
    return 1 if ASC_count > DESC_count else -1


def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()
    
    res = 0
    for line in lines:
        lis = list(map(int, line.split()))
        
        ASC = get_direction(lis)
        if ASC == 0: continue

        res += 1
        tolerated = False

        idx_managed = False
        for i in range(1, len(lis)):
            if idx_managed:
                idx_managed = False
                continue
            if not(1 <= (lis[i] - lis[i-1]) * ASC <= 3):
                if tolerated:
                    res -= 1
                    break

                if i == len(lis)-1:
                    break
                elif ((i == 1 and (1 <= (lis[2] - lis[0]) * ASC <= 3 or 1 <= (lis[2] - lis[1]) * ASC <= 3)) or 
                      (2 <= i <= len(lis)-2 and ((1 <= (lis[i+1] - lis[i-1]) * ASC <= 3) or 
                                                 (1 <= (lis[i+1] - lis[i]) * ASC <= 3 and 1 <= (lis[i] - lis[i-2]) * ASC <= 3)))):
                    idx_managed = True
                    tolerated = True
                else:
                    res -= 1
                    break

    return res

if __name__ == "__main__":
    assert solution("day2/test.txt") == 4
    print( solution("day2/data.txt") )
