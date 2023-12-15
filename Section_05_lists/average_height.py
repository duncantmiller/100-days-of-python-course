# calculate average without using sum() method

height_string = "151 145 179"
student_heights = height_string.split()
number_of_students = len(student_heights)

total_height = 0
for height in student_heights:
  total_height += int(height)

print(f"Total height: {total_height}")
print(f"Number of students: {number_of_students}")
print(f"Average height: {round(total_height / number_of_students, 2)}")
