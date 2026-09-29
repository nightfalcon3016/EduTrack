def display_dashboard(
    student,
    academic,
    performance,
    attendance,
    risk,
    current_cgpa
):
    print("\n" + "=" * 58)
    print("                    EDUTRACK")
    print("                 ACADEMIC DASHBOARD")
    print("=" * 58)

    print("\nSTUDENT INFORMATION")
    print("-" * 58)

    print(
        f"Name: {student['name']}"
    )

    print(
        f"Registration Number: "
        f"{student['registration_number']}"
    )

    print(
        f"Semester: {student['semester']}"
    )

    print("\nACADEMIC SUMMARY")
    print("-" * 58)

    print(
        f"SGPA: {performance['sgpa']:.2f}"
    )

    print(
        f"Current CGPA: {current_cgpa:.2f}"
    )

    print(
        f"Attendance: "
        f"{attendance['attendance']:.2f}%"
    )

    print(
        f"Attendance Status: "
        f"{attendance['status']}"
    )

    print(
        f"Academic Risk: "
        f"{risk['level']}"
    )

    print("\nATTENDANCE SAFE ZONE")
    print("-" * 58)

    if attendance["exemption"]:
        print(
            "Minimum attendance exemption currently applies."
        )

    elif attendance["classes_needed"] > 0:
        print(
            f"Classes required to reach "
            f"{attendance['threshold']}%: "
            f"{attendance['classes_needed']}"
        )

    else:
        print(
            f"Maximum additional absences within safe zone: "
            f"{attendance['safe_absences']}"
        )

    print("\nSUBJECT PERFORMANCE")
    print("-" * 58)

    for subject, result in performance["subjects"].items():
        print(
            f"{subject:<15}"
            f"Marks: {result['marks']:<7.1f}"
            f"Grade: {result['grade']:<4}"
            f"Credits: {result['credits']}"
        )

    print("\nACADEMIC HIGHLIGHTS")
    print("-" * 58)

    if performance["strong_subjects"]:
        print(
            "Strong Subjects: "
            + ", ".join(
                performance["strong_subjects"]
            )
        )

    else:
        print(
            "Strong Subjects: None identified"
        )

    if performance["weak_subjects"]:
        print(
            "Subjects Requiring Attention: "
            + ", ".join(
                performance["weak_subjects"]
            )
        )

    else:
        print(
            "Subjects Requiring Attention: None"
        )

    if academic["backlogs"]:
        print(
            "Backlogs: "
            + ", ".join(
                academic["backlogs"]
            )
        )

    else:
        print("Backlogs: None")

    print("=" * 58)