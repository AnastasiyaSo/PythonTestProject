"""Homework 14"""
# Task # 1

try:
    with open("students.txt", "w+", encoding="utf-8") as students_file:
        content = students_file.write("student1 group1 5\n"
                                      "student2 group1 5\n"
                                      "student3 group1 5\n"
                                      "student4 group2 5\n"
                                      "student5 group2 4\n"
                                      "student6 group2 3\n")

    with open("students.txt", "r", encoding="utf-8") as students_file:
        content1 = students_file.readlines()
        group1, marks1 = 0, 0
        group2, marks2 = 0, 0
        for line in content1:
            student, group, mark = line.split()
            if group == "group1":
                group1 += 1
                marks1 += int(mark)
            if group == "group2":
                group2 += 1
                marks2 += int(mark)
        total_students = group1 + group2
        marks1 = int(marks1 / group1)
        marks2 = int(marks2 / group2)
        print(total_students, marks1, marks2)

    with open("students.txt", "a", encoding="utf-8") as students_file:
        content2 = students_file.write(f"{total_students}, {marks1}, {marks2}")

except FileNotFoundError:
    print("FileNotFoundError")
