students = []


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i} (out of 100): "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nResult added successfully!\n")


def display_students():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n--- Student Results ---")

    for student in students:
        print(f"\nName       : {student['name']}")
        print(f"Roll No    : {student['roll_no']}")
        print(f"Total      : {student['total']}/500")
        print(f"Percentage : {student['percentage']:.2f}%")
        print(f"Grade      : {student['grade']}")


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n--- Student Found ---")
            print(f"Name       : {student['name']}")
            print(f"Roll No    : {student['roll_no']}")
            print(f"Total      : {student['total']}/500")
            print(f"Percentage : {student['percentage']:.2f}%")
            print(f"Grade      : {student['grade']}\n")
            return

    print("\nStudent not found.\n")


def main():
    while True:
        print("===== Student Result Management System =====")
        print("1. Add Student Result")
        print("2. Display All Results")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.\n")


main()
