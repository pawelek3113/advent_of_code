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


class Solution:
    def __init__(self, file) -> None:
        self.file = file
        self.input = self.get_input()
        self.combined_digits = self.get_combined_digits()
        self.sum = self.get_sum()

    def get_input(self) -> list[str]:
        with open(self.file, "r", encoding="UTF-8") as f:
            return f.read().splitlines()

    def get_combined_digits(self) -> list[int]:
        combined_digits = []

        digits = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            0: "zero",
        }

        for l in self.input:
            num = ""

            indexes = {}

            for k, v in digits.items():
                str_index = l.find(v)
                digit_index = l.find(str(k))

                if str_index != -1 or digit_index != -1:
                    index = min(str_index, digit_index)
                    if index == -1:
                        index = max(str_index, digit_index)
                    dct = {index: k}
                    indexes.update(dct)

            num += str(indexes[min(indexes.keys())])

            jdexes = {}

            for k, v in digits.items():
                str_index = l[::-1].find(v[::-1])
                digit_index = l[::-1].find(str(k))

                if str_index != -1 or digit_index != -1:
                    index = min(str_index, digit_index)
                    if index == -1:
                        index = max(str_index, digit_index)
                    dct = {index: k}
                    jdexes.update(dct)

            num += str(jdexes[min(jdexes.keys())])

            combined_digits.append(int(num))

        return combined_digits

    def get_sum(self) -> int:
        sum = 0
        for num in self.combined_digits:
            sum += num

        return sum


s = Solution("2023/01/input.txt")
print(s.sum)
