def find_max_joltage_bank_part_1(bank):
    """
    Find the maximum joltage possible from a single bank.
    Try all possible pairs of digits (i, j) where i < j.
    The joltage is formed by concatenating bank[i] and bank[j].
    """
    max_joltage = 0

    # Try all possible pairs (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form a 2-digit number from position i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)

    return max_joltage


# Open the file in read mode
file = open("input-sample.txt", "r")

# iterate though file
total_joltage = 0
for bank in file:
    max_joltage = find_max_joltage_bank_part_1(bank)
    # print(f"Bank {bank}: max joltage = {max_joltage}")
    total_joltage += max_joltage

print(total_joltage)
