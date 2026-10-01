"""result.py - Create, save, display and report exam results."""

import utils


def load_results():
    return utils.load_json(utils.RESULTS_FILE)


def save_results(results):
    return utils.save_json(utils.RESULTS_FILE, results)


def generate_result_id(results):
    """Create a unique ID like R001, R002 ..."""
    number = len(results) + 1
    existing_ids = [r.get("result_id") for r in results]
    while f"R{number:03d}" in existing_ids:
        number += 1
    return f"R{number:03d}"


def create_result(student, total_questions, attempted, correct,
                  total_marks, obtained_marks):
    """Build the result record, save it permanently and display it."""
    results = load_results()

    percentage = round((obtained_marks / total_marks) * 100, 2)
    record = {
        "result_id": generate_result_id(results),
        "student_id": student["student_id"],
        "student_name": student["name"],
        "date_time": utils.current_datetime(),
        "total_questions": total_questions,
        "attempted": attempted,
        "correct": correct,
        "wrong": attempted - correct,
        "total_marks": total_marks,
        "obtained_marks": obtained_marks,
        "percentage": percentage,
        "grade": utils.calculate_grade(percentage),
        "status": utils.get_status(percentage)
    }

    results.append(record)
    if save_results(results):
        print("\nResult saved successfully!")
    display_result(record)


def display_result(record):
    utils.print_header("EXAMINATION RESULT")
    print(f"Result ID        : {record['result_id']}")
    print(f"Student ID       : {record['student_id']}")
    print(f"Student Name     : {record['student_name']}")
    print(f"Date & Time      : {record['date_time']}")
    print(f"Total Questions  : {record['total_questions']}")
    print(f"Attempted        : {record['attempted']}")
    print(f"Correct Answers  : {record['correct']}")
    print(f"Wrong Answers    : {record['wrong']}")
    print(f"Total Marks      : {record['total_marks']}")
    print(f"Obtained Marks   : {record['obtained_marks']}")
    print(f"Percentage       : {record['percentage']:.2f}%")
    print(f"Grade            : {record['grade']}")
    print(f"Result           : {record['status']}")
    print("=" * 60)


def print_results_table(results):
    line = "-" * 94
    print(line)
    print(f"{'Result ID':<10}{'Student ID':<12}{'Name':<18}{'Date & Time':<21}"
          f"{'Marks':<10}{'Percent':<10}{'Grade':<7}{'Status':<6}")
    print(line)
    for r in results:
        marks = f"{r['obtained_marks']}/{r['total_marks']}"
        percent = f"{r['percentage']:.2f}%"
        print(f"{r['result_id']:<10}{r['student_id']:<12}{r['student_name'][:16]:<18}"
              f"{r['date_time']:<21}{marks:<10}{percent:<10}{r['grade']:<7}{r['status']:<6}")
    print(line)


def get_student_results(results, student_id):
    """Return all results of one student (case-insensitive ID)."""
    return [r for r in results if r["student_id"].upper() == student_id.upper()]


def view_student_result():
    utils.print_header("VIEW STUDENT RESULT")
    results = load_results()
    if not results:
        print("No results available. No exam has been taken yet.")
        return

    student_id = utils.get_non_empty("Enter Student ID: ")
    student_results = get_student_results(results, student_id)
    if not student_results:
        print("No result found for this Student ID.")
        return
    print("Showing the latest result:")
    display_result(student_results[-1])


def view_all_results():
    utils.print_header("ALL RESULTS")
    results = load_results()
    if not results:
        print("No results available. No exam has been taken yet.")
        return
    print_results_table(results)
    print(f"Total results: {len(results)}")


def search_result():
    utils.print_header("SEARCH RESULT BY STUDENT ID")
    results = load_results()
    if not results:
        print("No results available. No exam has been taken yet.")
        return

    keyword = utils.get_non_empty("Enter Student ID (full or partial): ").upper()
    matches = [r for r in results if keyword in r["student_id"].upper()]
    if not matches:
        print("No result found for this Student ID.")
        return
    print(f"{len(matches)} result(s) found:")
    print_results_table(matches)


def result_history():
    utils.print_header("RESULT HISTORY")
    results = load_results()
    if not results:
        print("No results available. No exam has been taken yet.")
        return

    student_id = utils.get_non_empty("Enter Student ID: ")
    student_results = get_student_results(results, student_id)
    if not student_results:
        print("No exam history found for this Student ID.")
        return

    print(f"\nExam history of {student_results[0]['student_name']} "
          f"({student_results[0]['student_id']})")
    print("-" * 70)
    for attempt, r in enumerate(student_results, start=1):
        print(f"Attempt {attempt}: {r['date_time']} | {r['result_id']} | "
              f"{r['obtained_marks']}/{r['total_marks']} | "
              f"{r['percentage']:.2f}% | Grade {r['grade']} | {r['status']}")
    print("-" * 70)
    print(f"Total attempts: {len(student_results)}")


def show_statistics():
    utils.print_header("RESULT STATISTICS")
    results = load_results()
    if not results:
        print("No results available. No exam has been taken yet.")
        return

    highest = max(results, key=lambda r: r["percentage"])
    average = sum(r["percentage"] for r in results) / len(results)
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed

    print(f"Total exam attempts : {len(results)}")
    print(f"Highest score       : {highest['obtained_marks']}/{highest['total_marks']} "
          f"({highest['percentage']:.2f}%) by {highest['student_name']} "
          f"[{highest['student_id']}]")
    print(f"Average percentage  : {average:.2f}%")
    print(f"Pass count          : {passed}")
    print(f"Fail count          : {failed}")


def result_menu():
    while True:
        utils.print_header("RESULTS & REPORTS")
        print("1. View Student Result (latest)")
        print("2. View All Results")
        print("3. Search Result by Student ID")
        print("4. Result History")
        print("5. Statistics (Highest, Average, Pass/Fail)")
        print("6. Back to Main Menu")
        choice = utils.get_menu_choice(1, 6)

        if choice == 1:
            view_student_result()
        elif choice == 2:
            view_all_results()
        elif choice == 3:
            search_result()
        elif choice == 4:
            result_history()
        elif choice == 5:
            show_statistics()
        else:
            break
