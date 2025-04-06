from student_utils.arithmetic import calculate_percentage, classify_grade
from student_utils.attendance import attendance_percent
from student_utils.performance import evaluate

marks = 85
total = 100

percentage = calculate_percentage(marks, total)
print(f"Percentage: {percentage:.2f}%")

grade = classify_grade(percentage)
print(f"Grade: {grade}")

attended = 2
total_classes = 10
attendance = attendance_percent(attended, total_classes)
print(f"Attendance: {attendance:.2f}%")

performance = evaluate(marks)
print(f"Performance: {performance}")

marks2 = 65
percentage2 = calculate_percentage(marks2, total)
print(f"\nFor marks {marks2}, Percentage: {percentage2:.2f}% and Grade: {classify_grade(percentage2)}")

attended2 = 5
attendance2 = attendance_percent(attended2, total_classes)
print(f"\nAttendance for 5 out of 10 classes: {attendance2:.2f}%")

marks3 = 45
performance3 = evaluate(marks3)
print(f"\nFor marks {marks3}, Performance: {performance3}")
