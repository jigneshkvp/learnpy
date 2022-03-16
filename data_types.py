# Lists
temperatues = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

# dictionary
student_grades = {"Mary": 8.8, "John": 7.5, "Viktor": 10.0}

grades_sum = sum(student_grades.values())
len_grades = len(student_grades)

mean_grades = grades_sum / len_grades

print(f"Mean grades={mean_grades}")
print(list(student_grades.values()))
print(f"Tens={list(student_grades.values()).count(10.0)}")

# tuples
heights = (10.0, 3.0, 5.4)
