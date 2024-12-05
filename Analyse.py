import os
import shutil
import timeit
import tracemalloc

from day1 import part1, part2

DAY = 1
SHOW_PART = [1, 2]
RUNS = 100
FILE_PATH = f"day{DAY}/data.txt"
SOLUTION = {1: part1.solution, 2: part2.solution}

def execution_time(func):
    execution_time = timeit.timeit(lambda: func(FILE_PATH), number=RUNS)
    return round(execution_time, 2)

def memory_used(func):
    tracemalloc.start()
    func(FILE_PATH)
    peak_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return round(peak_memory / 1024, 2)

def show_analysis_part(i):
    outcome = f"""
    =========PART {i}=========\n
    Execution time: {execution_time(SOLUTION[i])} seconds
    Memory used: {memory_used(SOLUTION[i])} KB\n
    """
    print(outcome)

if __name__ == "__main__":
    for i in SHOW_PART:
        show_analysis_part(i)
    if os.path.exists(f"day{DAY}/__pycache__"):
        shutil.rmtree(f"day{DAY}/__pycache__")
