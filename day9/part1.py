def solution(file):
    with open(file, "r") as f:
        disk_map = f.readline()
    
    blocks = [None if i % 2 else i//2 for i in range(len(disk_map)) for _ in range(int(disk_map[i]))]

    l, r = 0, len(blocks)-1
    res = 0
    while l <= r:
        if blocks[r] is None:
            r -= 1
            continue
        if blocks[l] is None:
            blocks[l] = blocks[r]
            r -= 1
        res += l * blocks[l]
        l += 1

    return res

if __name__ == "__main__":
    assert solution("day9/test.txt") == 1928
    print( solution("day9/data.txt") )
