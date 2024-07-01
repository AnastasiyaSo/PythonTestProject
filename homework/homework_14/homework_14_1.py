"""Homework 14"""
# Task # 1

try:
    students_data = [
        "Serena Williams", "1A", "[5,4,4,3]",
        "\nLionel Messi", "2B", "[4,3,5,2]",
        "\nKobe Bryant", "1A", "[3,5,4,1]"
    ]

    with open("students.txt", "w+", encoding="utf-8") as students_file:
        students_file.write(" ".join(students_data))

    with open("students.txt", "r", encoding="utf-8") as students_file:
        content1 = students_file.readlines()
        group1, marks1 = 0, 0.0
        group2, marks2 = 0, 0.0
        for line in content1:
            first_name, last_name, group, marks = line.split()
            marks_ = marks.strip("[ ]")
            marks_2 = marks_.split(",")
            marks_list = list(map(float, marks_2))
            number_of_marks = len(marks_list)
            if group == "1A":
                group1 += 1
                marks1 += sum(marks_list) / number_of_marks
            if group == "2B":
                group2 += 1
                marks2 += sum(marks_list) / number_of_marks
        total_students = group1 + group2
        total_marks1 = float(marks1 / group1)
        total_marks2 = float(marks2 / group2)
        print(total_students, total_marks1, total_marks2)

    with open("students.txt", "a", encoding="utf-8") as students_file:
        content2 = students_file.write(f"\nTotal students: {total_students}"
                                       f", Average rating of"
                                       f" \"1A\": {total_marks1}, "
                                       f"Average rating of"
                                       f" \"2B\": {total_marks2}")

except FileNotFoundError:
    print("FileNotFoundError")
