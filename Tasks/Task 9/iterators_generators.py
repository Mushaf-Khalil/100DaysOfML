import random

class StudentList:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

def attendance_generator(count):
    for _ in range(count):
        yield random.choice(["Present", "Absent"])

def random_marks_generator():
    while True:
        yield random.randint(0, 100)

if __name__ == "__main__":
    students = ["Ali", "Sara", "Tom"]
    print("Student List:")
    for s in StudentList(students):
        print(s)

    print("\\nAttendance:")
    for status in attendance_generator(3):
        print(status)

    print("\\nRandom Marks:")
    gen = random_marks_generator()
    for _ in range(5):
        print(next(gen))
