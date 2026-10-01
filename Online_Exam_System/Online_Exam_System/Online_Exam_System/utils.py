"""utils.py - Common helper functions used by all modules."""

import json
import os
import re
from datetime import datetime

# ---------- File paths (always relative to this file, so the project
# ---------- runs correctly from any folder) ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")
RESULTS_FILE = os.path.join(DATA_DIR, "results.json")


# ---------- JSON file handling ----------
def load_json(file_path):
    """Read a JSON list from a file. Returns [] if the file is missing,
    empty or damaged, so the program never crashes."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {os.path.basename(file_path)} is empty or damaged. "
              "Starting with empty data.")
        return []
    except OSError as error:
        print(f"Error reading file: {error}")
        return []


def save_json(file_path, data):
    """Write a list to a JSON file. Returns True if saved successfully."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving file: {error}")
        return False


def ensure_data_files():
    """Create the data folder and empty JSON files if they are missing."""
    os.makedirs(DATA_DIR, exist_ok=True)
    for path in (QUESTIONS_FILE, STUDENTS_FILE, RESULTS_FILE):
        if not os.path.exists(path):
            save_json(path, [])


# ---------- Input helpers ----------
def get_non_empty(prompt):
    """Keep asking until the user types something."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")


def get_positive_int(prompt):
    """Keep asking until the user enters a whole number greater than 0."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Error: Input cannot be empty. Please try again.")
            continue
        if not value.isdigit() or int(value) <= 0:
            print("Error: Please enter a whole number greater than 0.")
            continue
        return int(value)


def get_option_letter(prompt):
    """Keep asking until the user enters A, B, C or D."""
    while True:
        value = input(prompt).strip().upper()
        if value in ("A", "B", "C", "D"):
            return value
        print("Error: Please enter only A, B, C or D.")


def get_menu_choice(low, high):
    """Ask for a menu number between low and high (inclusive)."""
    while True:
        value = input("Enter your choice: ").strip()
        if value.isdigit() and low <= int(value) <= high:
            return int(value)
        print(f"Invalid choice. Please enter a number from {low} to {high}.")


def confirm(prompt):
    """Ask a yes/no question. Returns True for yes."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("y", "yes"):
            return True
        if value in ("n", "no"):
            return False
        print("Error: Please enter y or n.")


# ---------- Validation ----------
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def is_valid_name(name):
    return all(ch.isalpha() or ch in " .'" for ch in name)


def is_valid_student_id(student_id):
    return student_id.isalnum()


# ---------- Result helpers ----------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def get_status(percentage):
    return "PASS" if percentage >= 50 else "FAIL"


def current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ---------- Display helper ----------
def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)
