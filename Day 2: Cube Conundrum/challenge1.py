MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

MAX_COLORS = [MAX_RED, MAX_GREEN, MAX_BLUE]

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
    """Returns the maximum number of each color in a row."""
    states = preprocess_game_row(row) # Preprocess the row

    max_colors = {"red": 0, "green": 0, "blue": 0}
    for state in states:
        for count, color in state:
            max_colors[color] = max(max_colors[color], count)
    
    return max_colors

def game_id_from_row(row: str) -> int:
    """Returns the game ID from a row."""
    # The first number in each game ID starts at index 5
    # The game ID ends at the first colon
    game_id = row[5:row.index(':')]
    return int(game_id)

def sum_possible_game_ids(games: str) -> int:
    """Returns the sum of all possible game IDs."""
    total = 0

    rows = games.split("\n")
    for row in rows:
        max_colors = max_colors_in_row(row)
        state_possible = True
        for row_max, limit in zip(max_colors.values(), MAX_COLORS):
            if row_max > limit:
                state_possible = False
                break
        if state_possible:
            total += game_id_from_row(row)
    
    return total

if __name__ == "__main__":
    with open("game_states.txt", "r") as f:
        game = f.read()
    print(f"The total of the possible game states is {sum_possible_game_ids(game)}.")