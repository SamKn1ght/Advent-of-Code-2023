def calibration_number_from_line(line: str) -> int:
    """Returns the first and last number in a string as an integer."""
    first_number = None
    last_number = None
    for char in line:
        if char.isdigit():
            if first_number is None:
                first_number = char
            last_number = char
    return int(first_number + last_number)

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