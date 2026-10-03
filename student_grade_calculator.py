def calculate_grade(percentage):
    """Return a grade based on the student's percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    name = input("Enter student name: ")

    while True:
        try:
            number_of_subjects = int(input("Enter number of subjects: "))
            if number_of_subjects <= 0:
                print("Please enter at least 1 subject.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    total_marks = 0
    max_marks = 0

    for i in range(1, number_of_subjects + 1):
        print(f"\nSubject {i}")

        subject = input("Enter subject name: ")

        while True:
            try:
                maximum = float(input("Enter maximum marks: "))
                if maximum <= 0:
                    print("Maximum marks must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                marks = float(input(f"Enter marks obtained in {subject}: "))
                if marks < 0 or marks > maximum:
                    print(f"Marks must be between 0 and {maximum}.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        total_marks += marks
        max_marks += maximum

    percentage = (total_marks / max_marks) * 100
    grade = calculate_grade(percentage)

    print("\n" + "=" * 45)
    print("              RESULT")
    print("=" * 45)
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total_marks:.2f} / {max_marks:.2f}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")

    if grade == "F":
        print("Status       : Fail")
    else:
        print("Status       : Pass")

    print("=" * 45)


if __name__ == "__main__":
    main()
