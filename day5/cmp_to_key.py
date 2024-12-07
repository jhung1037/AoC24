from collections import defaultdict
from functools import cmp_to_key

def solution(file):
    with open(file, "r") as f:
        rules, updates = f.read().split("\n\n")
    
    front_of = defaultdict(set)
    for rule in rules.splitlines():
        a, b = rule.split("|")
        front_of[b].add(a)
    
    key = lambda a,b: -1 if a in front_of[b] else 1

    res = 0
    for update in updates.splitlines():
        pages = update.split(",")
        lis = sorted(pages, key=cmp_to_key(key))
        if lis != pages:
            res += int(lis[len(lis)//2])

    return res

if __name__ == "__main__":
    assert solution("day5/test.txt") == 123
    print( solution("day5/data.txt") )
