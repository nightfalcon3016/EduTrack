def analyze_risk(
    academic,
    performance,
    attendance
):
    risk_factors = []

    if attendance["status"] == "DEBARRED":
        risk_factors.append(
            "Attendance is below the required "
            "eligibility threshold."
        )

    if academic["backlogs"]:
        risk_factors.append(
            "The student has reported academic backlogs."
        )

    if performance["sgpa"] < 6:
        risk_factors.append(
            "Current semester performance requires "
            "significant improvement."
        )

    if performance["weak_subjects"]:
        risk_factors.append(
            "One or more subjects require "
            "additional academic attention."
        )

    if not risk_factors:
        risk_level = "LOW"

    elif len(risk_factors) >= 3:
        risk_level = "HIGH"

    else:
        risk_level = "MODERATE"

    return {
        "level": risk_level,
        "factors": risk_factors
    }


def display_risk(risk):
    print("\nACADEMIC RISK ANALYSIS")
    print("=" * 58)

    print(
        f"Risk Level: {risk['level']}"
    )

    print("\nIDENTIFIED FACTORS")
    print("-" * 58)

    if risk["factors"]:
        for number, factor in enumerate(
            risk["factors"],
            start=1
        ):
            print(
                f"{number}. {factor}"
            )

    else:
        print(
            "No significant academic risk factors identified."
        )