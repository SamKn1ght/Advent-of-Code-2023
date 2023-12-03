COLOR_NAMES = ["red", "green", "blue"]
DEFAULT_COUNT = [0] * len(COLOR_NAMES)

def preprocess_game_row(row: str) -> list:
    """
    Preprocesses the row given.
    
    Returns a list of states, where each state is a list of (number, color) pairs.
    """
    row = row[row.index(':') + 2:] # Removes the "Game x: "

    shown = row.split('; ') # Splits the row into shown states
    shown = [state.split(', ') for state in shown] # Splits each shown state into RGB values

    for i, state in enumerate(shown):
        shown[i] = [color.split(' ') for color in state] # Splits into (number, color) pairs
        for j, count in enumerate(shown[i]):
            shown[i][j] = (int(count[0]), count[1]) # Convert count to an int

    return shown

def max_colors_in_row(row: str) -> list[int, int, int]:
    """Returns the minimum possible number of each color in a row."""
    states = preprocess_game_row(row) # Preprocess the row

    max_colors = dict(zip(COLOR_NAMES, DEFAULT_COUNT))
    for state in states:
        for count, color in state:
            if count == 0:
                continue
            max_colors[color] = max(max_colors[color], count)
    
    return max_colors

from functools import reduce
from operator import mul

def power_of_set(arr: list) -> int:
    """Returns the power of the set of the given numbers."""
    return reduce(mul, arr)

def sum_powers_of_set(game: str) -> int:
    """Returns the sum of all possible game states."""
    total = 0

    rows = game.split("\n")
    for row in rows:
        min_color_counts = max_colors_in_row(row)
        total += power_of_set(min_color_counts.values())
    
    return total
    

if __name__ == "__main__":
    with open("game_states.txt", "r") as f:
        game = f.read()
    print(f"The total of the possible game states is {sum_powers_of_set(game)}.")