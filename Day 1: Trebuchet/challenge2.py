NAME_TO_NUMBER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
NUMBER_NAME_LENGTHS = [len(name) for name in NAME_TO_NUMBER.keys()]
MAX_NAME_LENGTH = max(NUMBER_NAME_LENGTHS)
MIN_NAME_LENGTH = min(NUMBER_NAME_LENGTHS)
SHARED_CHARACTERS_START_END = set()
for a in NAME_TO_NUMBER.keys():
    for b in NAME_TO_NUMBER.keys():
        if a == b:
            continue
        if a[0] == b[-1]:
            SHARED_CHARACTERS_START_END.add(b[-1])

def calibration_number_from_line(line: str) -> int:
    """
    Returns the first and last number in a string as an integer.
    Includes support for number names.
    """
    first_number = None
    last_number = None
    char_buffer = ""
    for char in line:
        if char.isdigit():
            if first_number is None:
                first_number = int(char)
            last_number = int(char)
            char_buffer = "" # No number names can start with a digit
        elif char.isalpha():
            char_buffer += char
            # Reduce the buffer size if it's too long
            if len(char_buffer) > MAX_NAME_LENGTH:
                char_buffer = char_buffer[1:]
            # Don't bother checking if the buffer is too short
            if len(char_buffer) < MIN_NAME_LENGTH:
                continue
            for length in range(MIN_NAME_LENGTH, MAX_NAME_LENGTH + 1):
                for start in range(MAX_NAME_LENGTH - length + 1):
                    # Check all possible substrings of the buffer that could be number names
                    sub_buffer = char_buffer[start:start + length]
                    if sub_buffer in NAME_TO_NUMBER:
                        if first_number is None:
                            first_number = NAME_TO_NUMBER[sub_buffer]
                        last_number = NAME_TO_NUMBER[sub_buffer]
                        cut_off = start + length # Cuts off all characters from this name
                        if sub_buffer[-1] in SHARED_CHARACTERS_START_END:
                            cut_off = start + length - 1 # Cuts off all characters except the last
                        char_buffer = char_buffer[cut_off:]
    return first_number * 10 + last_number

def calibration_document_sum(document: str) -> int:
    """Returns the sum of all numbers in the calibration document."""
    total = 0

    lines = document.split("\n")
    for line in lines:
        total += calibration_number_from_line(line)
    
    return total

if __name__ == "__main__":
    with open("calibration_document.txt", "r") as f:
        document = f.read()
    result = calibration_document_sum(document)
    print(f"The calibration document sum is {result}.")