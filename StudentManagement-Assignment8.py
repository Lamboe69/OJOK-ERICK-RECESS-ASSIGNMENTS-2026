import csv
import json
import os
import logging
from datetime import datetime

# Set up logging to file
logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

CSV_FILE = "students.csv"
JSON_FILE = "students.json"
CSV_HEADERS = ["reg_number", "name", "email"]


# Custom exception for student-related errors
class StudentError(Exception):
    pass


def log_action(action):
    """Log a user action to the log file."""
    logging.info(action)


def log_error(error):
    """Log an error to the log file."""
    logging.error(error)


def init_files():
    """Create CSV and JSON files with headers if they don't exist."""
    try:
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(CSV_HEADERS)
            log_action(f"Created {CSV_FILE} with headers")

        if not os.path.exists(JSON_FILE):
            with open(JSON_FILE, "w") as f:
                json.dump([], f)
            log_action(f"Created {JSON_FILE} with empty array")
    except IOError as e:
        log_error(f"File initialization failed: {e}")
        print(f"Error initializing files: {e}")


def read_csv():
    """Read all records from the CSV file and return as a list of dicts."""
    records = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        log_error("CSV file not found during read")
    except Exception as e:
        log_error(f"Unexpected error reading CSV: {e}")
    return records


def write_csv(records):
    """Write a list of dicts to the CSV file."""
    try:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(records)
    except Exception as e:
        log_error(f"Error writing to CSV: {e}")
        raise StudentError(f"Could not write to CSV: {e}")


def read_json():
    """Read additional details from the JSON file."""
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        log_error("JSON file not found during read")
    except json.JSONDecodeError as e:
        log_error(f"JSON decode error: {e}")
    except Exception as e:
        log_error(f"Unexpected error reading JSON: {e}")
    return []


def write_json(records):
    """Write additional details list to the JSON file."""
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(records, f, indent=4)
    except Exception as e:
        log_error(f"Error writing to JSON: {e}")
        raise StudentError(f"Could not write to JSON: {e}")


def find_student_index(records, reg_number):
    """Find the index of a student in the records list by registration number."""
    for i, rec in enumerate(records):
        if rec["reg_number"] == reg_number:
            return i
    return -1


def validate_email(email):
    """Basic email validation: must contain @ and ."""
    if "@" not in email or "." not in email:
        return False
    return True


def add_student():
    """Add a new student record."""
    print("\n--- Add New Student ---")
    reg = input("Enter registration number: ").strip()
    if not reg:
        print("Registration number cannot be empty.")
        return

    # Check for duplicate
    records = read_csv()
    if find_student_index(records, reg) != -1:
        print(f"Student with registration number '{reg}' already exists.")
        log_action(f"Failed to add student: duplicate reg number {reg}")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    email = input("Enter email: ").strip()
    if not validate_email(email):
        print("Invalid email format. Must contain '@' and '.'")
        return

    # Collect additional details for JSON
    address = input("Enter address: ").strip()
    contact = input("Enter contact number: ").strip()
    program = input("Enter program of study: ").strip()

    # Save to CSV
    try:
        records.append({
            "reg_number": reg,
            "name": name,
            "email": email,
        })
        write_csv(records)
        log_action(f"Added student {reg} to CSV")
    except StudentError as e:
        print(f"Failed to save: {e}")
        return

    # Save additional details to JSON
    try:
        json_data = read_json()
        json_data.append({
            "reg_number": reg,
            "address": address,
            "contact": contact,
            "program": program,
        })
        write_json(json_data)
        log_action(f"Added student {reg} details to JSON")
    except StudentError as e:
        print(f"Failed to save additional details: {e}")
        # Rollback CSV entry
        records.pop()
        write_csv(records)
        return

    print(f"Student '{name}' added successfully!")


def view_all_students():
    """Display all student records."""
    print("\n--- All Students ---")
    records = read_csv()
    if not records:
        print("No students found.")
        log_action("Viewed all students: no records")
        return

    print(f"{'Reg #':<15} {'Name':<25} {'Email':<30}")
    print("-" * 70)
    for rec in records:
        print(f"{rec['reg_number']:<15} {rec['name']:<25} {rec['email']:<30}")
    print(f"\nTotal: {len(records)} student(s)")
    log_action("Viewed all students")


def search_student():
    """Search for a student by registration number."""
    print("\n--- Search Student ---")
    reg = input("Enter registration number to search: ").strip()
    if not reg:
        print("Registration number cannot be empty.")
        return

    records = read_csv()
    idx = find_student_index(records, reg)
    if idx == -1:
        print(f"Student with registration '{reg}' not found.")
        log_action(f"Searched for student {reg}: not found")
        return

    rec = records[idx]
    print(f"\nRegistration: {rec['reg_number']}")
    print(f"Name: {rec['name']}")
    print(f"Email: {rec['email']}")

    # Fetch additional details from JSON
    json_data = read_json()
    for extra in json_data:
        if extra["reg_number"] == reg:
            print(f"Address: {extra.get('address', 'N/A')}")
            print(f"Contact: {extra.get('contact', 'N/A')}")
            print(f"Program: {extra.get('program', 'N/A')}")
            break

    log_action(f"Searched for student {reg}: found")


def update_student():
    """Update an existing student's details."""
    print("\n--- Update Student ---")
    reg = input("Enter registration number to update: ").strip()
    if not reg:
        print("Registration number cannot be empty.")
        return

    records = read_csv()
    idx = find_student_index(records, reg)
    if idx == -1:
        print(f"Student with registration '{reg}' not found.")
        log_action(f"Failed to update student {reg}: not found")
        return

    rec = records[idx]
    print(f"Updating: {rec['name']} ({rec['reg_number']})")
    print("Leave field blank to keep current value.")

    new_name = input(f"Name [{rec['name']}]: ").strip()
    if new_name:
        rec["name"] = new_name

    new_email = input(f"Email [{rec['email']}]: ").strip()
    if new_email:
        if not validate_email(new_email):
            print("Invalid email format.")
            return
        rec["email"] = new_email

    # Update CSV
    try:
        records[idx] = rec
        write_csv(records)
        log_action(f"Updated student {reg} in CSV")
    except StudentError as e:
        print(f"Failed to update CSV: {e}")
        return

    # Update JSON details
    json_data = read_json()
    for extra in json_data:
        if extra["reg_number"] == reg:
            addr = input(f"Address [{extra.get('address', '')}]: ").strip()
            if addr:
                extra["address"] = addr
            cnt = input(f"Contact [{extra.get('contact', '')}]: ").strip()
            if cnt:
                extra["contact"] = cnt
            prog = input(f"Program [{extra.get('program', '')}]: ").strip()
            if prog:
                extra["program"] = prog
            break
    else:
        # No JSON entry exists; create one
        addr = input("Address: ").strip()
        cnt = input("Contact: ").strip()
        prog = input("Program: ").strip()
        json_data.append({
            "reg_number": reg,
            "address": addr,
            "contact": cnt,
            "program": prog,
        })

    try:
        write_json(json_data)
        log_action(f"Updated student {reg} details in JSON")
    except StudentError as e:
        print(f"Failed to update JSON: {e}")
        return

    print(f"Student '{reg}' updated successfully!")


def delete_student():
    """Delete a student record."""
    print("\n--- Delete Student ---")
    reg = input("Enter registration number to delete: ").strip()
    if not reg:
        print("Registration number cannot be empty.")
        return

    records = read_csv()
    idx = find_student_index(records, reg)
    if idx == -1:
        print(f"Student with registration '{reg}' not found.")
        log_action(f"Failed to delete student {reg}: not found")
        return

    confirm = input(f"Delete {records[idx]['name']} ({reg})? (y/N): ").strip()
    if confirm.lower() != "y":
        print("Deletion cancelled.")
        return

    # Remove from CSV
    try:
        removed = records.pop(idx)
        write_csv(records)
        log_action(f"Deleted student {reg} from CSV")
    except StudentError as e:
        print(f"Failed to delete from CSV: {e}")
        return

    # Remove from JSON
    try:
        json_data = read_json()
        json_data = [j for j in json_data if j["reg_number"] != reg]
        write_json(json_data)
        log_action(f"Deleted student {reg} details from JSON")
    except StudentError as e:
        print(f"Failed to delete from JSON: {e}")
        # Rollback CSV
        records.insert(idx, removed)
        write_csv(records)
        return

    print(f"Student '{removed['name']}' deleted successfully!")


def main():
    """Main menu-driven loop."""
    init_files()
    print("=" * 60)
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 60)

    while True:
        try:
            print("\n--- Menu ---")
            print("1. Add a new student")
            print("2. View all students")
            print("3. Search for a student")
            print("4. Update student details")
            print("5. Delete a student record")
            print("6. Exit")
            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                view_all_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Goodbye!")
                log_action("User exited the system")
                break
            else:
                print("Invalid choice. Please enter 1-6.")
        except StudentError as e:
            print(f"System error: {e}")
            log_error(f"StudentError in main loop: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            log_action("User interrupted with Ctrl+C")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            log_error(f"Unexpected error in main loop: {e}")


if __name__ == "__main__":
    main()
