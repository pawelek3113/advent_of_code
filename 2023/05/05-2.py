"""
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5#part2

--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""

import re


class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"

    def intersection(self, interval: "Interval"):
        if interval.start >= self.end or interval.end <= self.start:
            return None
        else:
            return Interval(
                max(self.start, interval.start), min(self.end, interval.end)
            )


class Solution:
    def __init__(self, dir) -> None:
        self.dir = dir
        self.input = self.get_input()
        self.seed_intervals = self.get_seed_intervals()
        self.categories = self.get_categories()

        self.locations = self.get_locations()
        self.min_location = self.find_min_location()

    def get_input(self):
        with open(self.dir, "r", encoding="UTF-8") as file:
            return file.read().splitlines()

    def get_seed_intervals(self):
        with open(self.dir, "r", encoding="UTF-8") as file:
            seeds = [int(n) for n in (re.sub("seeds: ", "", file.readline()).split())]

            seed_intervals = [
                Interval(seeds[x], seeds[x] + seeds[x + 1] - 1)
                for x in range(0, len(seeds) - 1, 2)
            ]
        return seed_intervals

    def get_categories(self):
        file = open(self.dir, "r", encoding="UTF-8")
        categories = [
            [tuple(int(z) for z in y.split(" ")) for y in x.splitlines()[1:]]
            for x in file.read().strip().split("\n\n")[1:]
        ]

        return categories

    def _convert_interval(self, interval: Interval, scheme: tuple):
        dest, src, len = scheme
        shift = dest - src

        return Interval(interval.start + shift, interval.end + shift)

    def _convert_by_map(self, input: list[Interval], map):
        result = []

        while input:
            interval = input.pop()

            found = False
            for destination, source, range_length in map:
                map_interval = Interval(source, source + range_length)
                intersection = map_interval.intersection(interval)

                if not intersection:
                    continue
                else:
                    scheme = destination, source, range_length

                    converted_intersection = self._convert_interval(
                        intersection, scheme
                    )

                    res = []

                    res.append(converted_intersection)

                    if interval.start < intersection.start:
                        input.append(Interval(interval.start, intersection.start - 1))

                    if interval.end > intersection.end:
                        input.append(Interval(intersection.end + 1, interval.end))

                    result.extend(res)

                    found = True
                    break

            if not found:
                result.append(interval)

        return result

    def get_locations(self) -> list[Interval]:
        locations = []

        for seed_interval in self.seed_intervals:
            input = [seed_interval]

            for map in self.categories:
                input = self._convert_by_map(input, map)

            locations.extend(input)

        return locations

    def find_min_location(self):
        return min([x.start for x in self.locations])


s = Solution("2023/05/input.txt")

print(s.min_location)
