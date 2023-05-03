row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")


# Solution 1
X = int(position[0])
Y = int(position[1])
map[Y-1][X-1] = 'X'

# Solution 2
#X = int(position[0])
#Y = int(position[1])

#selected_row = map[Y -1]
#selected_row[X - 1] = 'X'


print(f"{row1}\n{row2}\n{row3}")