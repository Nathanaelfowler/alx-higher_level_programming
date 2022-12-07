#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for s1 in set_1:
        for s2 in set_2:
            set_3 = s1 | s2
    return set_3
