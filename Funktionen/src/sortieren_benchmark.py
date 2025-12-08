import time
import random
from sortieren import insertion_sort, selection_sort, bubble_sort, merge_sort

algos = [
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Bubble Sort", bubble_sort),
    ("Merge Sort", merge_sort),
]

def messung(sort_func, lst):
    start = time.perf_counter()
    sort_func(lst)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    sizes = [10, 100, 1000]
    print(f"{'Algorithmus':<15} {'Zufällig':>10} {'Sortiert':>10} {'Umgekehrt':>12}")
    for size in sizes:
        zufall = [random.randint(0, 10000) for _ in range(size)]
        sortiert = sorted(zufall)
        umgekehrt = list(reversed(sortiert))
        print(f"\nGröße: {size}")
        for name, func in algos:
            t1 = messung(func, zufall)
            t2 = messung(func, sortiert)
            t3 = messung(func, umgekehrt)
            print(f"{name:<15} {t1:10.6f} {t2:10.6f} {t3:12.6f}")
