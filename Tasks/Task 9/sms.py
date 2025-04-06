class Student:
    def __init__(self, name, age, student_id, courses):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = courses

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def calculate_gpa(self, grades):
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Courses: {', '.join(self.courses)}"


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, courses, thesis_title):
        super().__init__(name, age, student_id, courses)
        self.thesis_title = thesis_title

    def __str__(self):
        return f"{super().__str__()}, Thesis Title: {self.thesis_title}"

# Example Usage
if __name__ == "__main__":
    student = Student("Ali", 21, "ST101", ["Math", "CS"])
    print(student.get_name())
    grad_student = GraduateStudent("Sara", 24, "GR301", ["AI", "ML"], "AI for Healthcare")
    print(grad_student)
