from student import create_student_profile

from academic import (
    collect_academic_information
)

from academic_analyzer import (
    analyze_performance,
    calculate_current_cgpa
)

from attendance_analyzer import (
    analyze_attendance
)

from cgpa_simulator import (
    run_cgpa_simulator
)

from risk_analyzer import (
    analyze_risk,
    display_risk
)

from explanation_engine import (
    generate_explanation,
    display_explanation
)

from recommendation_engine import (
    generate_recommendations,
    display_recommendations
)

from dashboard import (
    display_dashboard
)

from storage import (
    save_student,
    get_student_history
)


def show_header():
    print("\n" + "=" * 58)
    print("                    EDUTRACK")
    print(
        "      Student Academic Performance & Eligibility Analyzer"
    )
    print("=" * 58)


def show_menu():
    print("\nMAIN MENU")
    print("-" * 58)

    print("1. Create Student Profile")
    print("2. Enter Academic Information")
    print("3. Academic Performance Analysis")
    print(
        "4. Attendance Compliance & Safe-Zone Analyzer"
    )
    print(
        "5. CGPA Goal & Performance Simulator"
    )
    print("6. Academic Risk Analysis")
    print(
        "7. Academic Performance Explanation"
    )
    print("8. Academic Recommendations")
    print("9. Academic Dashboard")
    print("10. Academic History")
    print("0. Exit")

    print("-" * 58)


def display_performance(performance):
    print(
        "\nACADEMIC PERFORMANCE ANALYSIS"
    )
    print("=" * 58)

    for subject, result in performance[
        "subjects"
    ].items():

        print(
            f"{subject:<15}"
            f"Marks: {result['marks']:<7.1f}"
            f"Grade: {result['grade']:<4}"
            f"Grade Point: {result['grade_point']}"
        )

    print("-" * 58)

    print(
        f"SGPA: {performance['sgpa']:.2f}"
    )

    print("\nSUBJECT RANKING")
    print("-" * 58)

    for position, (
        subject,
        result
    ) in enumerate(
        performance["ranked_subjects"],
        start=1
    ):

        print(
            f"{position}. "
            f"{subject} - "
            f"{result['marks']:.1f}"
        )

    print("\nSTRONG SUBJECTS")
    print("-" * 58)

    if performance["strong_subjects"]:
        print(
            ", ".join(
                performance["strong_subjects"]
            )
        )

    else:
        print(
            "No subjects currently meet "
            "the strong-performance level."
        )

    print(
        "\nSUBJECTS REQUIRING ATTENTION"
    )
    print("-" * 58)

    if performance["weak_subjects"]:
        print(
            ", ".join(
                performance["weak_subjects"]
            )
        )

    else:
        print(
            "No subjects currently require "
            "immediate attention."
        )


def display_attendance(attendance):
    print(
        "\nATTENDANCE COMPLIANCE & SAFE-ZONE ANALYZER"
    )
    print("=" * 58)

    print(
        f"Current Attendance: "
        f"{attendance['attendance']:.2f}%"
    )

    print(
        f"Required Threshold: "
        f"{attendance['threshold']}%"
    )

    print(
        f"Status: {attendance['status']}"
    )

    if attendance["exemption"]:

        print(
            "\nAttendance exemption is currently "
            "applicable based on the available "
            "academic information."
        )

    elif attendance["classes_needed"] > 0:

        print(
            f"\nClasses Required to Reach "
            f"{attendance['threshold']}%: "
            f"{attendance['classes_needed']}"
        )

    else:

        print(
            "\nMaximum Additional Absences "
            "Within Safe Zone: "
            f"{attendance['safe_absences']}"
        )


def display_history(history):
    print("\nACADEMIC HISTORY")
    print("=" * 58)

    if not history:
        print(
            "No saved academic history found."
        )
        return

    for record in history:

        student = record.get(
            "student",
            {}
        )

        performance = record.get(
            "performance",
            {}
        )

        attendance = record.get(
            "attendance",
            {}
        )

        current_cgpa = record.get(
            "current_cgpa"
        )

        print(
            f"\nSemester {student.get('semester', 'N/A')}"
        )

        print("-" * 58)

        print(
            f"SGPA: "
            f"{performance.get('sgpa', 0):.2f}"
        )

        if current_cgpa is not None:
            print(
                f"CGPA: "
                f"{current_cgpa:.2f}"
            )

        else:
            print("CGPA: N/A")

        print(
            f"Attendance: "
            f"{attendance.get('attendance', 0):.2f}%"
        )

        print(
            f"Status: "
            f"{attendance.get('status', 'N/A')}"
        )


def prepare_analysis(academic):
    performance = analyze_performance(
        academic
    )

    current_cgpa = calculate_current_cgpa(
        academic,
        performance["sgpa"]
    )

    attendance = analyze_attendance(
        academic,
        current_cgpa
    )

    risk = analyze_risk(
        academic,
        performance,
        attendance
    )

    return (
        performance,
        attendance,
        risk,
        current_cgpa
    )


def main():
    student = None
    academic = None
    performance = None
    attendance = None
    risk = None
    current_cgpa = None

    show_header()

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "0":

            print(
                "\nThank you for using EduTrack."
            )

            break

        elif choice == "1":

            student = create_student_profile()

            academic = None
            performance = None
            attendance = None
            risk = None
            current_cgpa = None

            print(
                "\nStudent profile created successfully."
            )

            print("-" * 40)

            print(
                f"Name: {student['name']}"
            )

            print(
                f"Registration Number: "
                f"{student['registration_number']}"
            )

            print(
                f"Semester: "
                f"{student['semester']}"
            )

        elif choice == "2":

            if student is None:

                print(
                    "\nPlease create a student "
                    "profile first."
                )

            else:

                academic = (
                    collect_academic_information(
                        student["semester"]
                    )
                )

                performance = None
                attendance = None
                risk = None
                current_cgpa = None

                print(
                    "\nAcademic information "
                    "saved successfully."
                )

        elif choice == "3":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                display_performance(
                    performance
                )

                print(
                    f"\nCurrent CGPA: "
                    f"{current_cgpa:.2f}"
                )

        elif choice == "4":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                display_attendance(
                    attendance
                )

        elif choice == "5":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                run_cgpa_simulator(
                    academic,
                    performance
                )

        elif choice == "6":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                display_risk(
                    risk
                )

        elif choice == "7":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                explanations = (
                    generate_explanation(
                        academic,
                        performance,
                        attendance,
                        risk
                    )
                )

                display_explanation(
                    explanations,
                    risk
                )

        elif choice == "8":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                recommendations = (
                    generate_recommendations(
                        academic,
                        performance,
                        attendance,
                        risk
                    )
                )

                display_recommendations(
                    recommendations
                )

        elif choice == "9":

            if academic is None:

                print(
                    "\nPlease enter academic "
                    "information first."
                )

            else:

                (
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                ) = prepare_analysis(
                    academic
                )

                display_dashboard(
                    student,
                    academic,
                    performance,
                    attendance,
                    risk,
                    current_cgpa
                )

                record = {
                    "student": student,
                    "academic": academic,
                    "performance": performance,
                    "attendance": attendance,
                    "risk": risk,
                    "current_cgpa": current_cgpa
                }

                save_student(
                    record
                )

                print(
                    "\nAcademic record "
                    "saved successfully."
                )

        elif choice == "10":

            if student is None:

                print(
                    "\nPlease create a student "
                    "profile first."
                )

            else:

                history = (
                    get_student_history(
                        student[
                            "registration_number"
                        ]
                    )
                )

                display_history(
                    history
                )

        else:

            print(
                "\nInvalid choice. "
                "Please select a valid option."
            )


if __name__ == "__main__":
    main()