import sys, os

with open('2.input', 'r') as input:
    data = input.read()

# Part 1

x = 0
y = 0
for data_point in data.splitlines():
    action, qty = data_point.split(" ")
    if action == "forward":
        x += int(qty)
    elif action == "down":
        y += int(qty)
    elif action == "up":
        y -= int(qty)

print (x * y)

# Part 2

x = 0
y = 0
aim = 0
for data_point in data.splitlines():
    action, qty = data_point.split(" ")
    if action == "forward":
        x += int(qty)
        y += aim * int(qty)
    elif action == "down":
        aim += int(qty)
    elif action == "up":
        aim -= int(qty)

print (x * y)
