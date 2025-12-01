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

    if direction == "L":
        position = position - length
    elif direction == "R":
        position = position + length

    if position > 99 or position < 0:
        position = position % 100

    if position == 0:
        password += 1

    # print(f"The dial now points at {position}")

print(f"num_lines: {num_lines}")
print(f"final password: {password}")


# Close the file
file.close()