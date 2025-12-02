def find_repeated_digit_sequences(start, end):
    """
    Find numbers with some sequence of digits repeated twice consecutively.
    For example: 11 (1 repeated), 1212 (12 repeated), 123123 (123 repeated)
    """
    result = []

    for num in range(start, end + 1):
        s = str(num)
        length = len(s)

        # Try all possible substring lengths (from 1 to half the string length)
        for sub_len in range(1, length // 2 + 1):
            if length % sub_len == 0 and length // sub_len == 2:
                # Check if first half equals second half
                if s[:sub_len] == s[sub_len:sub_len * 2]:
                    result.append(num)
                    break

    return result


def parse_range_string(range_str):
    """
    Parse a range string like '11-22' into a tuple (11, 22).
    """
    start, end = range_str.strip().split('-')
    return int(start), int(end)


def parse_input_file(filename):
    """
    Parse input file containing comma-separated ranges.
    Returns a list of (start, end) tuples.
    """
    with open(filename, 'r') as f:
        content = f.read().strip()

    ranges = []
    for range_str in content.split(','):
        ranges.append(parse_range_string(range_str))

    return ranges


def process_all_ranges(ranges):
    """
    Process all ranges and find matching numbers.
    Returns a list of all matching numbers across all ranges.
    """
    all_matches = []

    for start, end in ranges:
        matches = find_repeated_digit_sequences(start, end)
        all_matches.extend(matches)

    return all_matches


def calculate_sum_from_file(filename):
    """
    Main function to parse file and calculate sum of all matching numbers.
    """
    ranges = parse_input_file(filename)
    matches = process_all_ranges(ranges)
    total_sum = sum(matches)

    return total_sum, matches


# Main execution
if __name__ == "__main__":
    # Process the file
    total_sum, matches = calculate_sum_from_file('input-full.txt')

    # print(f"Matching numbers: {matches}")
    print(f"Total sum: {total_sum}")
