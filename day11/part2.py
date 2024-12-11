def dfs(num, rounds_left, dp):
    if rounds_left == 0: return 1
    if (num, rounds_left) in dp:
        return dp[(num, rounds_left)]

    if num == 0:
        dp[(0, rounds_left)] = dfs(1, rounds_left - 1, dp)
        return dp[(0, rounds_left)]
    else:
        length = len(str(num))
        if length % 2:
            dp[(num, rounds_left)] = dfs(num * 2024, rounds_left - 1, dp)
        else:
            q = 10 ** (length // 2)
            dp[(num, rounds_left)] = (dfs(num // q, rounds_left - 1, dp) + 
                                      dfs(num % q, rounds_left - 1, dp))
        return dp[(num, rounds_left)]

def solution(file):
    with open(file, "r") as f:
        stones = list(map(int, f.readline().split()))

    dp = {}
    res = sum(dfs(stone, 75, dp) for stone in stones)

    return res

if __name__ == "__main__":
    print( solution("day11/data.txt") )
