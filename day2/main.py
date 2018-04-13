"""
Day 2 - Part 1 & 2
"""

import data

def compute(row):
    for i in row.content:
        for j in row.content:
            if (i != j) & (i%j==0):
                return i/j    

with open("inputs/day2", "r") as f:
    read_data = f.read()
f.close()

d = data.parse(read_data)

res1 = 0
res2 = 0
for row in d.rows:
    res1 += (row.max - row.min)
    res2 += compute(row)

print "Part1 : " + str(res1) + ", Part2 : " + str(res2)
