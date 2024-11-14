# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# sorted_students = sorted(list(students))
#
# average_grade = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(grades[1])),(sum(grades[2]) / len(
# grades[2])),(sum(grades[3]) / len(grades[3])),(sum(grades[4]) / len(grades[4]))]
#
# average_grades = dict(zip(sorted_students, average_grade))
# print(average_grades)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

average_grades = {}

for x in range(len(sorted_students)):
    student_name = sorted_students[x]
    student_grades = grades[x]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[student_name] = average_grade

print(average_grades)