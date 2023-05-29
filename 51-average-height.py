student_heights = input("Input a list of student heights: ").split()

total_height = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    total_height += int(student_heights[n])

average_height = total_height / (len(student_heights))


print(student_heights)
print(f"Average height: {round(average_height)}")
