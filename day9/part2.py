def solution(file):
    with open(file, "r") as f:
        disk_map = f.readline()
    
    disk_map = [int(digit) for digit in disk_map]

    starting_index = [0]
    for i, num in enumerate(disk_map):
        starting_index.append(starting_index[i] + num)

    res = 0
    file_idx = len(disk_map) - 1
    file_num = len(disk_map) // 2
    while file_idx > 0:
        space_idx = 1
        compressed = False
        while space_idx < file_idx:
            if disk_map[space_idx] >= disk_map[file_idx]:
                res += file_num * (2 * starting_index[space_idx] + disk_map[file_idx] - 1) * disk_map[file_idx] // 2 
                disk_map[space_idx] -= disk_map[file_idx]
                starting_index[space_idx] += disk_map[file_idx]
                compressed = True
                break
            space_idx += 2
        if not compressed:
            res += file_num * (2 * starting_index[file_idx] + disk_map[file_idx] - 1) * disk_map[file_idx] // 2
        file_idx -= 2
        file_num -= 1

    return res

if __name__ == "__main__":
    assert solution("day9/test.txt") == 2858
    print( solution("day9/data.txt") )
