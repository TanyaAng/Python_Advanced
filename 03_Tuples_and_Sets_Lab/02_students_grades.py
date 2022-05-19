students_number=int(input())
students={}
for _ in range (students_number):
    student, grade_string = input().split()
    grade=float(grade_string)
    if student not in students:
        students[student]=[]
    students[student].append(grade)

for student, grades in students.items():
    grades_formatted=' '.join([f"{g:.2f}" for g in grades])
    average_grade=sum(grades)/len(grades)
    print(f"{student} -> {grades_formatted} (avg: {average_grade:.2f})")
