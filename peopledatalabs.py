#!/usr/bin/env python3

import json
import requests

# 1 2 3
# 4 5 6
# 7 8 9

keypads = {
    1 : {  'U' : 1, 'D': 4, 'L': 1, 'R' : 2 },
    2 : {  'U' : 2, 'D': 5, 'L': 1, 'R' : 3 },
    3 : {  'U' : 3, 'D': 6, 'L': 2, 'R' : 3 },
    4 : {  'U' : 1, 'D': 7, 'L': 4, 'R' : 5 },
    5 : {  'U' : 2, 'D': 8, 'L': 4, 'R' : 6 },
    6 : {  'U' : 3, 'D': 9, 'L': 5, 'R' : 6 },
    7 : {  'U' : 4, 'D': 7, 'L': 7, 'R' : 8 },
    8 : {  'U' : 5, 'D': 8, 'L': 7, 'R' : 9 },
    9 : {  'U' : 6, 'D': 9, 'L': 8, 'R' : 9 }
}

start_key = 5
next_key = 0
combination = []

#response = requests.get("https://adventofcode.com/2016/day/2/input")

with open(r'./keypad-moves.txt', 'r') as fp:
    for line in fp:
        moves = list(line.rstrip())
        total_moves = len(moves)
        count = 0
        for move in moves:
            start_key = keypads[start_key][move]
            count += 1
            if count == total_moves:
                combination.append(start_key)

print(combination)
