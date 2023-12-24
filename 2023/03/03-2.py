"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3#part2

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""
import re
from operator import mul
from functools import reduce

content: list[str]

with open("2023/03/input.txt", "r", encoding="UTF-8") as file:
    content = file.read().splitlines()

# checking for symbol
pattern = r"\*"

numbers_and_gears: list[dict[int, list[tuple]]] = []

for idx, line in enumerate(content):
    numbers = re.findall(r"\d+", line)

    last_idx = 0

    for number in numbers:
        start_idx = line.find(number, last_idx)
        end_idx = len(str(number)) + start_idx - 1

        gears = []

        found = False

        # left side checking
        if re.match(pattern, line[start_idx - 1]):
            found = True
            gear_pos = (idx, start_idx - 1)
            gears.append(gear_pos)

        # right side checking
        if re.match(pattern, line[end_idx + int(1 if end_idx != len(line) - 1 else 0)]):
            found = True
            gear_pos = (idx, end_idx + int(1 if end_idx != len(line) - 1 else 0))
            gears.append(gear_pos)

        # up&down checking
        for u in range(
            start_idx - 1, end_idx + int(2 if end_idx != len(line) - 1 else 1)
        ):
            if idx != 0 and re.match(pattern, content[idx - 1][u]):
                found = True
                gear_pos = (idx - 1, u)
                gears.append(gear_pos)
            if idx != len(content) - 1 and re.match(pattern, content[idx + 1][u]):
                found = True
                gear_pos = (idx + 1, u)
                gears.append(gear_pos)

        last_idx = end_idx
        if found:
            numbers_and_gears.append({int(number): gears})

results = {}

for info in numbers_and_gears:
    for num, gear_poses in info.items():
        for gear_pos in gear_poses:
            if gear_pos not in results.keys():
                results[gear_pos] = [num]
            else:
                number_list: list[int] = results[gear_pos]
                number_list.append(num)

sum = 0
for gear_pos, numbers in results.items():
    if len(numbers) == 2:
        sum += reduce(mul, numbers)

print(sum)
