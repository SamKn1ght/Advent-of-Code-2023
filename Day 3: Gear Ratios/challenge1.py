def dimensions(schematic: list) -> tuple:
    """Returns the dimensions of the schematic."""
    return len(schematic[0]), len(schematic)

def is_symbol(char: str) -> bool:
    """Returns True if the given character is a symbol."""
    return not (char.isalnum() or char == '.')

def is_horizontally_adjacent(a: tuple, b: tuple) -> bool:
    """
    Returns True if the given coordinates are adjacent to each other.

    Coordinates must be in the form (y, x).
    """
    return (abs(a[1] - b[1]) == 1 and a[0] == b[0])

def sum_part_numbers(schematic: str) -> int:
    """Returns the sum of all part numbers in the schematic."""
    schematic = schematic.split("\n")
    width, height = dimensions(schematic)

    part_number_dict = {}
    part_number_lengths = {}
    symbol_coordinates = []

    y = 0
    number_buffer = ""
    coordinate_buffer = []
    while y < height:
        x = 0
        number_buffer = ""
        coordinate_buffer = []
        while x < width:
            if schematic[y][x].isdigit():
                number_buffer += schematic[y][x]
                coordinate_buffer.append((y, x))
            elif number_buffer != "":
                for coordinate in coordinate_buffer:
                    part_number_dict[coordinate] = int(number_buffer)
                    part_number_lengths[coordinate] = len(number_buffer)
                number_buffer = ""
                coordinate_buffer = []
            if x == width - 1:
                for coordinate in coordinate_buffer:
                    part_number_dict[coordinate] = int(number_buffer)
                    part_number_lengths[coordinate] = len(number_buffer)
                number_buffer = ""
                coordinate_buffer = []
            if is_symbol(schematic[y][x]):
                symbol_coordinates.append((y, x))
            x += 1
        y += 1
    
    coordinates_to_check = set()
    for c in symbol_coordinates:
        for y in range(c[0] - 1, c[0] + 2):
            for x in range(c[1] - 1, c[1] + 2):
                if y < 0 or y >= height:
                    break
                if x < 0 or x >= width:
                    continue
                if (y, x) in part_number_dict:
                    coordinates_to_check.add((y, x))
    
    to_remove = set()
    protected = set()
    for c in coordinates_to_check:
        if c in part_number_dict:
            protected.add(c)
            length = part_number_lengths[c]
            for i in range(c[1] - length, c[1] + length + 1):
                if i == c[1]:
                    continue
                if (c[0], i) in protected:
                    continue
                if part_number_dict[c] == part_number_dict.get((c[0], i)):
                    if (c[0], i) in coordinates_to_check:
                        to_remove.add((c[0], i))
    for c in to_remove:
        coordinates_to_check.remove(c)

    return sum(part_number_dict[c] for c in coordinates_to_check)


if __name__ == "__main__":
    with open("engine_schematic.txt", "r") as f:
        file = f.read()
    print(f"The sum of all part numbers is {sum_part_numbers(file)}.")