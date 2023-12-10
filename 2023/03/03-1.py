"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
import re


content: list[str]

with open("2023/03/input.txt", "r", encoding="UTF-8") as file:
    content = file.read().splitlines()

adjacent_numbers = [0]

# checking for symbol
pattern = r"[!@#$%^&*()_+\-{}\[\]:;<>,?~\\/\|=]"

for idx, line in enumerate(content):
    numbers = re.findall(r"\d+", line)

    last_idx = 0

    for number in numbers:
        start_idx = line.find(number, last_idx)
        end_idx = len(str(number)) + start_idx - 1

        found = False
        # side-checking
        if re.match(pattern, line[start_idx - 1]) or re.match(
            pattern, line[end_idx + int(1 if end_idx != len(line) - 1 else 0)]
        ):
            found = True

        # up&down checking
        for u in range(
            start_idx - 1, end_idx + int(2 if end_idx != len(line) - 1 else 1)
        ):
            if found:
                break

            if idx != 0 and re.match(pattern, content[idx - 1][u]):
                found = True
            if idx != len(content) - 1 and re.match(pattern, content[idx + 1][u]):
                found = True

        last_idx = end_idx
        if found:
            adjacent_numbers.append(int(number))


sum = sum(adjacent_numbers)
print(sum)
