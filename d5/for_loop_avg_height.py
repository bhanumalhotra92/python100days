student_height = input("Input a list of student heights  ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

sum_of_height = 0
for height in student_height:
    sum_of_height += height
print(sum_of_height)

num_of_student = 0
for student in student_height:
    num_of_student += 1
print(num_of_student)

avg_height = round(sum_of_height / num_of_student)
print(f"Average height : {avg_height}")
