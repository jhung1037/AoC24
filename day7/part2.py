def recur_check(ans, nums, i):
    num = int(nums[i])
    if i == 0:
        return True if num == ans else False
    if ans % num == 0 and recur_check(ans//num, nums, i-1):
        return True
    if ans - num >= 0 and recur_check(ans-num, nums, i-1):
        return True
    if (ans - num) % (10**len(nums[i])) == 0 and recur_check((ans-num)//(10**len(nums[i])), nums, i-1):
        return True
    return False

def solution(file):
    with open(file, "r") as f:
        lines = f.readlines()

    res = 0
    for line in lines:
        str_ans, str_nums = line.split(":", 1)
        nums = str_nums.split()
        ans = int(str_ans)
        if recur_check(ans, nums, len(nums)-1):
            res += ans

    return res

if __name__ == "__main__":
    assert solution("day7/test.txt") == 11387
    print( solution("day7/data.txt") )
