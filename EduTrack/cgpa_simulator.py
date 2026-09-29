CURRENT_SEMESTER_CREDITS = 16


def calculate_projected_cgpa(
    current_cgpa,
    current_credits,
    future_sgpa,
    future_credits
):
    total_credits = (
        current_credits + future_credits
    )

    if total_credits == 0:
        return current_cgpa

    return (
        (current_cgpa * current_credits)
        + (future_sgpa * future_credits)
    ) / total_credits


def calculate_required_sgpa(
    current_cgpa,
    current_credits,
    target_cgpa,
    future_credits
):
    if future_credits == 0:
        return 0

    return (
        target_cgpa
        * (current_credits + future_credits)
        - current_cgpa * current_credits
    ) / future_credits


def get_target_cgpa():
    while True:
        try:
            target = float(
                input("Target CGPA: ")
            )

            if 0 <= target <= 10:
                return target

            print("Enter CGPA between 0 and 10.")

        except ValueError:
            print("Enter a valid number.")


def run_cgpa_simulator(
    academic,
    performance
):
    print(
        "\nCGPA GOAL & ACADEMIC PERFORMANCE SIMULATOR"
    )
    print("=" * 58)

    semester = int(
        academic["semester"]
    )

    if semester == 1:
        current_cgpa = performance["sgpa"]
        current_credits = CURRENT_SEMESTER_CREDITS

    else:
        previous_cgpa = academic["previous_cgpa"]
        previous_credits = academic["previous_credits"]

        current_cgpa = (
            (
                previous_cgpa
                * previous_credits
            )
            + (
                performance["sgpa"]
                * CURRENT_SEMESTER_CREDITS
            )
        ) / (
            previous_credits
            + CURRENT_SEMESTER_CREDITS
        )

        current_credits = (
            previous_credits
            + CURRENT_SEMESTER_CREDITS
        )

    target_cgpa = get_target_cgpa()

    required_sgpa = calculate_required_sgpa(
        current_cgpa,
        current_credits,
        target_cgpa,
        CURRENT_SEMESTER_CREDITS
    )

    print("\nCURRENT ACADEMIC POSITION")
    print("-" * 58)

    print(
        f"Current SGPA: "
        f"{performance['sgpa']:.2f}"
    )

    print(
        f"Current CGPA: "
        f"{current_cgpa:.2f}"
    )

    print(
        f"Target CGPA: "
        f"{target_cgpa:.2f}"
    )

    print("\nTARGET ANALYSIS")
    print("-" * 58)

    if current_cgpa >= target_cgpa:
        print(
            "The target CGPA has already been reached."
        )

        if required_sgpa <= 10:
            print(
                f"Next-semester SGPA required to "
                f"remain at or above the target: "
                f"{required_sgpa:.2f}"
            )

    elif required_sgpa <= 10:
        print(
            f"Required Next-Semester SGPA: "
            f"{required_sgpa:.2f}"
        )

    else:
        print(
            f"Required Next-Semester SGPA: "
            f"{required_sgpa:.2f}"
        )

        print(
            "The target cannot be reached in one "
            "semester under the current credit configuration."
        )

    print("\nPERFORMANCE SCENARIOS")
    print("-" * 58)

    for sgpa in [7, 8, 9, 10]:
        projected = calculate_projected_cgpa(
            current_cgpa,
            current_credits,
            sgpa,
            CURRENT_SEMESTER_CREDITS
        )

        print(
            f"If Next SGPA = {sgpa:.1f}"
            f"  ->  Projected CGPA = "
            f"{projected:.2f}"
        )