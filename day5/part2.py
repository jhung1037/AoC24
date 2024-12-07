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
        valid = True
        for i in range(len(page)):
            for j in range(i+1, len(page)):
                if page[j] in front_of[page[i]]:
                    page[i], page[j] = page[j], page[i]
                    valid = False
            if not valid and i == len(page)//2:
                break
        if not valid:
            res += int(page[len(page)//2])

    return res

if __name__ == "__main__":
    assert solution("day5/test.txt") == 123
    print( solution("day5/data.txt") )
