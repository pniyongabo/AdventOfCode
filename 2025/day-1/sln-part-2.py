# Open the file in read mode
file = open("input-full.txt", "r")

# Read the entire content of the file
# content = file.read()
# print(content)

# Reading a file line by line
num_lines = 0
position = 50
password = 0

for line in file:
    num_lines += 1
    direction = line[0]
    length = int(line[1:])

    # Count full rotations (each full 100 = 1 zero crossing)
    full_rotations = length // 100
    password += full_rotations

    # Handle remainder movement
    remainder = length % 100
    if remainder > 0:
        if direction == "L":
            new_position = position - remainder
        else:  # direction == "R"
            new_position = position + remainder

        # Check if we crossed zero during this movement
        if direction == "L" and new_position < 1 and position > 0:
            password += 1
        elif direction == "R" and new_position >= 100:  # and position < 100:
            password += 1

        # Wrap position to stay in 0-99 range
        position = (new_position + 100) % 100

    # print(f"The dial now points at {position}, total zero crossings so far: {password}")

print(f"num_lines: {num_lines}")
print(f"final password: {password}")


# Close the file
file.close()
