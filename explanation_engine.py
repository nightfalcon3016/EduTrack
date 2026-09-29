def generate_explanation(
    academic,
    performance,
    attendance,
    risk
):
    explanations = []

    if attendance["exemption"]:
        explanations.append(
            "The attendance status reflects the applicable "
            "high-CGPA attendance exemption because the "
            "available academic information shows a CGPA "
            "of at least 9.00 and no reported backlogs."
        )

    elif attendance["attendance"] < attendance["threshold"]:
        explanations.append(
            f"Attendance is "
            f"{attendance['attendance']:.2f}%, "
            f"which is below the required "
            f"{attendance['threshold']}% threshold."
        )

    else:
        explanations.append(
            f"Attendance is "
            f"{attendance['attendance']:.2f}%, "
            f"which meets the required "
            f"{attendance['threshold']}% threshold."
        )

    if performance["sgpa"] >= 9:
        explanations.append(
            f"The current SGPA of "
            f"{performance['sgpa']:.2f} indicates "
            "strong semester performance."
        )

    elif performance["sgpa"] >= 7:
        explanations.append(
            f"The current SGPA of "
            f"{performance['sgpa']:.2f} indicates "
            "satisfactory semester performance."
        )

    else:
        explanations.append(
            f"The current SGPA of "
            f"{performance['sgpa']:.2f} indicates "
            "that academic performance requires improvement."
        )

    if performance["strong_subjects"]:
        explanations.append(
            "Strong performance was recorded in: "
            + ", ".join(
                performance["strong_subjects"]
            )
            + "."
        )

    if performance["weak_subjects"]:
        explanations.append(
            "Additional attention is recommended for: "
            + ", ".join(
                performance["weak_subjects"]
            )
            + "."
        )

    if academic["backlogs"]:
        explanations.append(
            "The reported backlog subjects are: "
            + ", ".join(
                academic["backlogs"]
            )
            + "."
        )

    else:
        explanations.append(
            "No academic backlogs have been reported."
        )

    return explanations


def display_explanation(
    explanations,
    risk
):
    print(
        "\nACADEMIC PERFORMANCE EXPLANATION"
    )
    print("=" * 58)

    print("WHY DID I GET THIS RESULT?")
    print("-" * 58)

    for number, explanation in enumerate(
        explanations,
        start=1
    ):
        print(
            f"{number}. {explanation}"
        )

    print("\nOVERALL INTERPRETATION")
    print("-" * 58)

    if risk["level"] == "HIGH":
        print(
            "Multiple academic factors require immediate "
            "attention. The identified factors should be "
            "addressed systematically."
        )

    elif risk["level"] == "MODERATE":
        print(
            "Some academic factors require attention. "
            "Improving the identified areas can strengthen "
            "the overall academic position."
        )

    else:
        print(
            "No significant academic risk factors were "
            "identified from the available information."
        )