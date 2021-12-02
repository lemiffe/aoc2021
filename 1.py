import sys, os

with open('1.input', 'r') as input:
    data = input.read()
data = [int(a) for a in data.splitlines()]

# Part 1

prev_value = None
increases = 0
for num in data:
    if prev_value is not None and num > prev_value:
        increases += 1
    prev_value = num

print (increases)

# Part 2 (windowed / look-behind) <- Wrong!

prev_value = None
increases = 0
for i in range (2, len(data) - 1):
    sum_window = data[i - 2] + data[i - 1] + data[i]
    if prev_value is not None and sum_window > prev_value:
        increases += 1
    prev_value = sum_window

print(increases)

# Part 2 (windowed / look-ahead) <- Correct!

prev_value = None
increases = 0
for i in range (0, len(data) - 1):
    if (i + 3) < len(data):
        window_a = data[i] + data[i + 1] + data[i + 2]
        window_b = data[i + 1] + data[i + 2] + data[i + 3]
        if window_b > window_a:
            increases += 1

print(increases)
