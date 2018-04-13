"""
Day 1 - Part 1 & 2
"""

def compute(data, step_forward):
    res = 0
    for i in range(len(data)): #len(data) not included in the generated value
        comparable_index = (i + step_forward) % len(data)
        if data[i] == data[comparable_index]:
            res += int(data[i])

    return res

with open("inputs/day1", "r") as f:
    read_data = f.read()
f.close()

print "** Day 1 **"
print "Part1: " + str(compute(read_data, 1))
print "Part2: " + str(compute(read_data, len(read_data)/2))
