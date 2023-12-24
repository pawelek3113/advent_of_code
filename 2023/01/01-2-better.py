"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1#part2

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

# include first and last letter
# case: eightwo

mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


class Solution:
    def __init__(self, file) -> None:
        self.file = file
        self.input = self.map_input()
        self.combined_digits = self.get_combined_digits()
        self.sum = self.get_sum()

    def get_input(self) -> str:
        with open(self.file, "r", encoding="UTF-8") as f:
            return f.read()

    def map_input(self) -> list[str]:
        data = self.get_input()
        for name, alias in mapping.items():
            data = data.replace(name, alias)

        return data.splitlines()

    def get_combined_digits(self) -> list[int]:
        combined_digits = []
        for l in self.input:
            num = ""
            for char in l:
                if char.isdigit():
                    num += char
                    break
            for char in l[::-1]:
                if char.isdigit():
                    num += char
                    break

            combined_digits.append(int(num))
        return combined_digits

    def get_sum(self) -> int:
        sum = 0
        for num in self.combined_digits:
            sum += num

        return sum


s = Solution("2023/01/input.txt")
print(s.sum)
