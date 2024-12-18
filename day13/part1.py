import re

def solution(file):
    with open(file, "r") as f:
        combinations = f.read().split("\n\n")
    
    res = 0
    for combination in combinations:
        a1, a2, b1, b2, c1, c2 = list(map(int, re.findall("\d+", combination)))
        x = (b2*c1-b1*c2) / (a1*b2-b1*a2)
        y = (a2*c1-a1*c2) / (b1*a2-a1*b2)
        if int(x) == x and int(y) == y:
            res += 3 * x + y

    return int(res)

if __name__ == "__main__":
    assert solution("day13/test.txt") == 480
    print( solution("day13/data.txt") )
