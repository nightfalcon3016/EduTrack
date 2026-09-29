import json
import os


DATA_FILE = "data/students.json"


def ensure_data_file():
    folder = os.path.dirname(DATA_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(DATA_FILE):
        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump([], file)


def load_students():
    ensure_data_file()

    try:
        with open(
            DATA_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

    except (
        json.JSONDecodeError,
        OSError
    ):
        pass

    return []


def save_student(record):
    students = load_students()

    registration_number = (
        record["student"]["registration_number"]
    )

    semester = record["student"]["semester"]

    updated = False

    for index, existing_record in enumerate(students):
        existing_student = existing_record.get(
            "student",
            {}
        )

        if (
            existing_student.get(
                "registration_number"
            )
            == registration_number
            and existing_student.get(
                "semester"
            )
            == semester
        ):
            students[index] = record
            updated = True
            break

    if not updated:
        students.append(record)

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            students,
            file,
            indent=4
        )


def get_student_history(
    registration_number
):
    students = load_students()

    history = []

    for record in students:
        student = record.get(
            "student",
            {}
        )

        if (
            student.get("registration_number")
            == registration_number
        ):
            history.append(record)

    history.sort(
        key=lambda record: int(
            record.get(
                "student",
                {}
            ).get(
                "semester",
                0
            )
        )
    )

    return history