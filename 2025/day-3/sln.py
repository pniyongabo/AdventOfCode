from itertools import combinations


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


def find_max_joltage_bank_part_2_brute_force(bank):
    """
    Find the maximum joltage possible from a single bank.
    Pick exactly 12 digits from the bank (maintaining order) to form
    the largest possible 12-digit number.
    """
    max_joltage = 0

    # Try all possible combinations of 12 positions
    for positions in combinations(range(len(bank)), 12):
        # Form a 12-digit number from the selected positions
        joltage_str = ''.join(bank[i] for i in positions)
        joltage = int(joltage_str)
        max_joltage = max(max_joltage, joltage)

    return max_joltage


def find_max_joltage_bank_part_2_optimized(bank):
    max_total_joltage = bank[:12]
    for i in range(12, len(bank)):
        current_joltage = bank[i]
        for i in range(12):
            temp = max_total_joltage[0:i] + max_total_joltage[i+1:12] + current_joltage
            if int(temp) > int(max_total_joltage):
                max_total_joltage = temp
                break
    return int(max_total_joltage)


# Open the file in read mode
file = open("input-full.txt", "r")

# iterate though file
total_joltage = 0
for bank in file:
    max_joltage = find_max_joltage_bank_part_2_optimized(bank)
    total_joltage += max_joltage

print(total_joltage)
