students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

total_class = 0

for s in range(1, students + 1):
    print("Student", s)
    total_student = 0

    for sub in range(1, subjects + 1):
        score = float(input("Enter score " + str(sub) + ": "))
        total_student += score

    avg_student = total_student / subjects
    print("Average for Student", s, "=", avg_student)
    total_class += avg_student

class_avg = total_class / students
print("Class Average =", class_avg)
