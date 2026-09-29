SUBJECTS = {
    "Physics": 4,
    "Chemistry": 4,
    "Mathematics": 4,
    "English": 3,
    "UHV": 1
}


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))

            if 0 <= mark <= 100:
                return mark

            print("Enter marks between 0 and 100.")

        except ValueError:
            print("Enter a valid number.")


def get_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))

            if value >= minimum:
                return value

            print(f"Enter a value of {minimum} or above.")

        except ValueError:
            print("Enter a valid whole number.")


def get_cgpa(prompt):
    while True:
        try:
            cgpa = float(input(prompt))

            if 0 <= cgpa <= 10:
                return cgpa

            print("Enter CGPA between 0 and 10.")

        except ValueError:
            print("Enter a valid number.")


def get_backlogs():
    while True:
        answer = input("Backlogs? (Y/N): ").strip().upper()

        if answer == "N":
            return []

        if answer == "Y":
            subjects = input("Backlog Subjects: ").strip()

            if subjects:
                return [
                    subject.strip()
                    for subject in subjects.split(",")
                    if subject.strip()
                ]

            print("Enter at least one backlog subject.")

        else:
            print("Enter Y or N.")


def collect_academic_information(semester):
    semester = int(semester)

    print("\nACADEMIC INFORMATION")
    print("-" * 40)

    marks = {}

    print("\nMARKS")
    print("-" * 40)

    for subject in SUBJECTS:
        marks[subject] = get_mark(subject)

    print("\nATTENDANCE")
    print("-" * 40)

    classes_attended = get_integer(
        "Classes Attended: ",
        0
    )

    total_classes = get_integer(
        "Total Classes: ",
        1
    )

    while total_classes < classes_attended:
        print("Total classes cannot be less than classes attended.")

        total_classes = get_integer(
            "Total Classes: ",
            1
        )

    backlogs = get_backlogs()

    previous_cgpa = None
    previous_credits = 0

    if semester > 1:
        print("\nPREVIOUS ACADEMIC RECORD")
        print("-" * 40)

        previous_cgpa = get_cgpa(
            "Previous CGPA: "
        )

        previous_credits = get_integer(
            "Completed Credits Before Current Semester: ",
            1
        )

    return {
        "semester": semester,
        "marks": marks,
        "credits": SUBJECTS.copy(),
        "classes_attended": classes_attended,
        "total_classes": total_classes,
        "previous_cgpa": previous_cgpa,
        "previous_credits": previous_credits,
        "backlogs": backlogs
    }