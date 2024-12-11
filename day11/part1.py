def solution(file):
    with open(file, "r") as f:
        stones = list(map(int, f.readline().split()))
    
    for _ in range(25):
        for i in range(len(stones)):
            if stones[i] == 0:
                stones[i] = 1
            else:
                length = len(str(stones[i]))
                if length % 2:
                    stones[i] = stones[i] * 2024
                else:
                    q = 10 ** (length // 2)
                    stones.append(stones[i] % q)
                    stones[i] = stones[i] // q

    return len(stones)

if __name__ == "__main__":
    assert solution("day11/test.txt") == 55312
    print( solution("day11/data.txt") )
