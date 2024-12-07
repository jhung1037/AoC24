from collections import defaultdict

def solution(file):
    with open(file, "r") as f:
        rules, updates = f.read().split("\n\n")
    
    front_of = defaultdict(set)
    for rule in rules.splitlines():
        a, b = rule.split("|")
        front_of[b].add(a)
    
    res = 0
    for pages in updates.splitlines():
        page = pages.split(",")
        if all(page[i] in front_of[page[j]] for i in range(len(page)) for j in range(i+1, len(page))): 
            res += int(page[len(page)//2])

    return res

if __name__ == "__main__":
    assert solution("day5/test.txt") == 143
    print( solution("day5/data.txt") )
