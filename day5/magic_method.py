from collections import defaultdict

class Key():
    def __init__(self, page, front_of):
        self.page = page
        self.front_of = front_of
    
    def __lt__(self, others):
        return self.page in self.front_of[others.page]
    
    def __int__(self):
        return int(self.page)

def solution(file):
    with open(file, "r") as f:
        rules, updates = f.read().split("\n\n")
    
    front_of = defaultdict(set)
    for rule in rules.splitlines():
        a, b = rule.split("|")
        front_of[b].add(a)
    
    res = 0
    for update in updates.splitlines():
        pages = update.split(",")
        lis = [Key(page, front_of) for page in pages]
        sorted_lis = sorted(lis)
        if sorted_lis != lis:
            res += int(sorted_lis[len(sorted_lis)//2])

    return res

if __name__ == "__main__":
    assert solution("day5/test.txt") == 123
    print( solution("day5/data.txt") )
