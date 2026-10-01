"""student_manager.py - Register, view and search students."""

import utils


def load_students():
    return utils.load_json(utils.STUDENTS_FILE)


def save_students(students):
    return utils.save_json(utils.STUDENTS_FILE, students)


def find_student(students, student_id):
    """Return the student with the given ID (case-insensitive), or None."""
    for student in students:
        if student.get("student_id", "").upper() == student_id.upper():
            return student
    return None


def print_students_table(students):
    print("-" * 70)
    print(f"{'Student ID':<14}{'Name':<25}{'Email':<31}")
    print("-" * 70)
    for student in students:
        print(f"{student['student_id']:<14}{student['name']:<25}{student['email']:<31}")
    print("-" * 70)


def register_student():
    utils.print_header("REGISTER STUDENT")
    students = load_students()

    # Student ID must be unique
    while True:
        student_id = utils.get_non_empty("Enter Student ID (letters/digits, e.g. S101): ").upper()
        if not utils.is_valid_student_id(student_id):
            print("Error: Student ID can contain only letters and digits (no spaces).")
        elif find_student(students, student_id) is not None:
            print("Error: This Student ID already exists. Try another ID.")
        else:
            break

    while True:
        name = utils.get_non_empty("Enter student name: ")
        if utils.is_valid_name(name):
            break
        print("Error: Name can contain only letters and spaces.")

    while True:
        email = utils.get_non_empty("Enter email: ").lower()
        if utils.is_valid_email(email):
            break
        print("Error: Invalid email format (example: name@example.com).")

    students.append({"student_id": student_id, "name": name, "email": email})
    if save_students(students):
        print("Student registered successfully!")


def view_students():
    utils.print_header("ALL STUDENTS")
    students = load_students()
    if not students:
        print("No students registered yet.")
        return
    print_students_table(students)
    print(f"Total students: {len(students)}")


def search_student():
    utils.print_header("SEARCH STUDENT")
    students = load_students()
    if not students:
        print("No students registered yet.")
        return

    keyword = utils.get_non_empty("Enter Student ID or name: ").lower()
    matches = [s for s in students
               if keyword in s["student_id"].lower() or keyword in s["name"].lower()]

    if not matches:
        print("Student not found.")
        return
    print(f"{len(matches)} student(s) found:")
    print_students_table(matches)


def student_menu():
    while True:
        utils.print_header("STUDENT MANAGEMENT")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Back to Main Menu")
        choice = utils.get_menu_choice(1, 4)

        if choice == 1:
            register_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        else:
            break
