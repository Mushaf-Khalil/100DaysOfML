def read_students(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
            print(f"\\nTotal students: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Something went wrong: {e}")

def write_students(filename, student_data):
    try:
        with open(filename, 'w') as f:
            for student in student_data:
                f.write(student + '\\n')
        print("Data written successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    # Example Usage
    data = ["Ali, 21, ST101, Math", "Sara, 24, GR301, AI"]
    write_students("student_output.txt", data)
    read_students("student_output.txt")
