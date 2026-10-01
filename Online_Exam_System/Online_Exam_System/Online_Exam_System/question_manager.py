"""question_manager.py - Add, view, search, update and delete questions."""

import utils

OPTION_LETTERS = ["A", "B", "C", "D"]


def load_questions():
    return utils.load_json(utils.QUESTIONS_FILE)


def save_questions(questions):
    return utils.save_json(utils.QUESTIONS_FILE, questions)


def find_question(questions, question_id):
    """Return the question with the given ID, or None if not found."""
    for question in questions:
        if question.get("id") == question_id:
            return question
    return None


def display_question(question):
    print("-" * 60)
    print(f"ID       : {question['id']}")
    print(f"Question : {question['question']}")
    for letter in OPTION_LETTERS:
        print(f"   {letter}. {question['options'][letter]}")
    print(f"Correct  : {question['answer']}")
    print(f"Marks    : {question['marks']}")


def add_question():
    utils.print_header("ADD QUESTION")
    questions = load_questions()

    # Question ID must be unique
    while True:
        question_id = utils.get_positive_int("Enter Question ID (number): ")
        if find_question(questions, question_id) is not None:
            print("Error: This Question ID already exists. Try another ID.")
        else:
            break

    text = utils.get_non_empty("Enter question: ")

    options = {}
    for letter in OPTION_LETTERS:
        while True:
            option = utils.get_non_empty(f"Enter option {letter}: ")
            if option.lower() in [o.lower() for o in options.values()]:
                print("Error: This option is already used. Enter a different one.")
            else:
                options[letter] = option
                break

    answer = utils.get_option_letter("Enter correct answer (A/B/C/D): ")
    marks = utils.get_positive_int("Enter marks for this question: ")

    questions.append({
        "id": question_id,
        "question": text,
        "options": options,
        "answer": answer,
        "marks": marks
    })
    if save_questions(questions):
        print("Question added successfully!")


def view_questions():
    utils.print_header("ALL QUESTIONS")
    questions = load_questions()
    if not questions:
        print("No questions available. Please add questions first.")
        return
    for question in questions:
        display_question(question)
    print("-" * 60)
    print(f"Total questions: {len(questions)}")


def search_question():
    utils.print_header("SEARCH QUESTION")
    questions = load_questions()
    if not questions:
        print("No questions available. Please add questions first.")
        return

    keyword = utils.get_non_empty("Enter Question ID or keyword: ").lower()
    matches = []
    for question in questions:
        if keyword == str(question["id"]) or keyword in question["question"].lower():
            matches.append(question)

    if not matches:
        print("Question not found.")
        return
    print(f"{len(matches)} question(s) found:")
    for question in matches:
        display_question(question)


def update_question():
    utils.print_header("UPDATE QUESTION")
    questions = load_questions()
    if not questions:
        print("No questions available. Please add questions first.")
        return

    question_id = utils.get_positive_int("Enter Question ID to update: ")
    question = find_question(questions, question_id)
    if question is None:
        print("Question not found.")
        return

    display_question(question)
    print("\nPress Enter to keep the current value.")

    new_text = input("New question text: ").strip()
    if new_text:
        question["question"] = new_text

    for letter in OPTION_LETTERS:
        new_option = input(f"New option {letter}: ").strip()
        if new_option:
            question["options"][letter] = new_option

    while True:
        new_answer = input("New correct answer (A/B/C/D): ").strip().upper()
        if new_answer == "":
            break
        if new_answer in OPTION_LETTERS:
            question["answer"] = new_answer
            break
        print("Error: Please enter only A, B, C or D (or press Enter to skip).")

    while True:
        new_marks = input("New marks: ").strip()
        if new_marks == "":
            break
        if new_marks.isdigit() and int(new_marks) > 0:
            question["marks"] = int(new_marks)
            break
        print("Error: Marks must be a whole number greater than 0 (or press Enter to skip).")

    if save_questions(questions):
        print("Question updated successfully!")


def delete_question():
    utils.print_header("DELETE QUESTION")
    questions = load_questions()
    if not questions:
        print("No questions available. Please add questions first.")
        return

    question_id = utils.get_positive_int("Enter Question ID to delete: ")
    question = find_question(questions, question_id)
    if question is None:
        print("Question not found.")
        return

    display_question(question)
    if utils.confirm("Are you sure you want to delete this question? (y/n): "):
        questions.remove(question)
        if save_questions(questions):
            print("Question deleted successfully!")
    else:
        print("Delete cancelled.")


def question_menu():
    while True:
        utils.print_header("QUESTION MANAGEMENT")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Search Question")
        print("4. Update Question")
        print("5. Delete Question")
        print("6. Back to Main Menu")
        choice = utils.get_menu_choice(1, 6)

        if choice == 1:
            add_question()
        elif choice == 2:
            view_questions()
        elif choice == 3:
            search_question()
        elif choice == 4:
            update_question()
        elif choice == 5:
            delete_question()
        else:
            break
