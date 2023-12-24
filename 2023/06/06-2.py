"""
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6#part2

--- Part Two ---
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?
"""

import re
from functools import reduce
from operator import mul


class Solution:
    def __init__(self, dir):
        self.dir = dir
        self.sheet_of_paper = self.get_sheet_of_paper()
        self.wins = self.determine_wins()
        self.answer = self.get_answer()

    def get_sheet_of_paper(self):
        with open(self.dir, "r", encoding="UTF-8") as file:
            numbers = [
                [int(y) for y in re.findall(r"\d+", row)]
                for row in file.read().splitlines()
            ]

            res = []
            for row in numbers:
                res.append(int("".join(map(str, row))))

            return res

    def determine_wins(self):
        races = []

        time = self.sheet_of_paper[0]
        distance = self.sheet_of_paper[1]

        wins = 0

        for hold_time in range(1, time + 1):
            velocity = hold_time
            remaining_time = time - hold_time
            travelled_distance = velocity * remaining_time

            if travelled_distance > distance:
                wins += 1

        races.append(wins)

        return races

    def get_answer(self):
        return reduce(mul, self.wins)


s = Solution("input.txt")

print(s.answer)
