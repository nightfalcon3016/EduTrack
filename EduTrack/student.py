def get_semester():
    while True:
        try:
            semester = int(input("Semester: "))

            if 1 <= semester <= 8:
                return semester

            print("Enter a semester between 1 and 8.")

        except ValueError:
            print("Enter a valid semester number.")


def create_student_profile():
    print("\nSTUDENT PROFILE")
    print("-" * 40)

    name = input("Student Name: ").strip()
    registration_number = input("Registration Number: ").strip()
    semester = get_semester()

    return {
        "name": name,
        "registration_number": registration_number,
        "semester": semester
    }