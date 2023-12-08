"""
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2#part2

--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

import re
from pprint import pprint
class Solution():
    def __init__(self, dir) -> None:
        self.dir = dir
        self.games = self.get_games()
        self.sum = self.get_sum()
    
    def get_games(self) -> list[list[dict]]:
        games = []
        with open(self.dir, "r", encoding="UTF-8") as file:
            for line in file:
                pattern = r"^Game \d+:"
                sets = re.sub(pattern, "", line).strip().split(";")
                sets = [set.strip() for set in sets]
                
                sets_dicts = []

                for set in sets:
                    dict = {}

                    for cube in set.split(","):
                        amount, color = cube.strip().split()
                        dict.update({color: int(amount)})

                    sets_dicts.append(dict)

                games.append(sets_dicts)
        
        return games

    def get_fewest_cubes(self) -> list[tuple]:
        games = []
        for game in self.games:
            max_red = max_green = max_blue = 0

            for set in game:
                for color, amount in set.items():
                    if color == "red":
                        if amount > max_red:
                            max_red = amount
                    
                    elif color == "green":
                        if amount > max_green:
                            max_green = amount
                    
                    elif color == "blue":
                        if amount > max_blue:
                            max_blue = amount
            
            games.append([max_red, max_green, max_blue])

        return games

    def get_powers(self):
        powers = []
        for red, green, blue in self.get_fewest_cubes():
            powers.append(red*green*blue)
        
        return powers

    def get_sum(self) -> int:
        sum = 0
        for power in self.get_powers():
            sum += power

        return sum
       

s = Solution("2023/02/input.txt")

pprint(s.sum)