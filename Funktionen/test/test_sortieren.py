from sortieren import insertion_sort, selection_sort, bubble_sort, merge_sort
import pytest

unsorted = [5, 2, 9, 1, 5, 6]
sorted_list = [1, 2, 5, 5, 6, 9]
reverse = [9, 6, 5, 5, 2, 1]
empty = []
single = [42]

@pytest.mark.parametrize("func", [insertion_sort, selection_sort, bubble_sort, merge_sort])
def test_sort_correctness(func):
    assert func(unsorted) == sorted_list
    assert func(reverse) == sorted_list
    assert func(empty) == []
    assert func(single) == [42]
    # Eingabeliste bleibt unverändert
    assert unsorted == [5, 2, 9, 1, 5, 6]
    assert reverse == [9, 6, 5, 5, 2, 1]
