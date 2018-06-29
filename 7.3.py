#!/usr/bin/env python

def is_build_pos(small, large, goal):
    ileDuzych = 0
    while True:
        if (ileDuzych + 1) * 5 > goal or ileDuzych + 1 > large:
            break
        ileDuzych += 1
    if (goal - ileDuzych * 5) <= small:
        return True
    else:
        return False


print(is_build_pos(9,0,10))