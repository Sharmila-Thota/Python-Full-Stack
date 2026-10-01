"""exam.py - Conduct the online examination for a registered student."""

import utils
import student_manager
import question_manager
import result


def get_answer():
    """Ask for A/B/C/D, or S to skip. Repeats until input is valid."""
    while True:
        answer = input("Your answer (A/B/C/D, or S to skip): ").strip().upper()
        if answer in ("A", "B", "C", "D", "S"):
            return answer
        print("Error: Invalid input. Enter A, B, C, D or S.")


def start_exam():
    utils.print_header("START EXAMINATION")

    students = student_manager.load_students()
    if not students:
        print("No students registered. Please register a student first.")
        return

    questions = question_manager.load_questions()
    if not questions:
        print("No questions available. Please add questions first.")
        return

    student_id = utils.get_non_empty("Enter your Student ID: ")
    student = student_manager.find_student(students, student_id)
    if student is None:
        print("Student not found. Please register first.")
        return

    print(f"\nWelcome, {student['name']}!")
    print(f"Total questions : {len(questions)}")
    print("Enter A, B, C or D to answer, or S to skip a question.")
    print("Correct answers will be shown only in the final result.")
    if not utils.confirm("Start the exam now? (y/n): "):
        print("Exam cancelled.")
        return

    attempted = 0
    correct = 0
    total_marks = 0
    obtained_marks = 0

    for number, question in enumerate(questions, start=1):
        print("\n" + "-" * 60)
        print(f"Question {number} of {len(questions)}   [{question['marks']} mark(s)]")
        print(question["question"])
        for letter in question_manager.OPTION_LETTERS:
            print(f"   {letter}. {question['options'][letter]}")

        answer = get_answer()
        total_marks += question["marks"]

        if answer != "S":
            attempted += 1
            if answer == question["answer"]:
                correct += 1
                obtained_marks += question["marks"]

    print("\nExam finished. Calculating your result...")
    result.create_result(student, len(questions), attempted, correct,
                         total_marks, obtained_marks)
