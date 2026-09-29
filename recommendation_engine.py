def generate_recommendations(
    academic,
    performance,
    attendance,
    risk
):
    recommendations = []

    if attendance["exemption"]:
        recommendations.append(
            "Maintain consistent attendance even while "
            "the current attendance exemption applies."
        )

    elif attendance["attendance"] < attendance["threshold"]:
        recommendations.append(
            "Priority 1: Improve attendance and attend "
            "upcoming classes consistently until the "
            "required eligibility threshold is reached."
        )

    elif attendance["attendance"] < 80:
        recommendations.append(
            "Priority 1: Maintain consistent attendance "
            "because the current attendance level is "
            "relatively close to the threshold."
        )

    if performance["weak_subjects"]:
        subjects = ", ".join(
            performance["weak_subjects"]
        )

        recommendations.append(
            f"Priority 2: Focus additional preparation "
            f"on {subjects}."
        )

    if academic["backlogs"]:
        subjects = ", ".join(
            academic["backlogs"]
        )

        recommendations.append(
            f"Priority 3: Address the reported backlog "
            f"subjects: {subjects}."
        )

    if performance["sgpa"] < 6:
        recommendations.append(
            "Increase preparation consistency and "
            "strengthen fundamental concepts before "
            "moving to advanced topics."
        )

    elif performance["sgpa"] < 8:
        recommendations.append(
            "Strengthen preparation in lower-performing "
            "subjects to improve overall semester performance."
        )

    elif performance["weak_subjects"]:
        recommendations.append(
            "Maintain strong performance in high-performing "
            "subjects while giving additional attention "
            "to weaker subjects."
        )

    else:
        recommendations.append(
            "Maintain the current study pattern and "
            "continue consistent academic preparation."
        )

    if risk["level"] == "HIGH":
        recommendations.append(
            "Follow the identified priorities systematically "
            "because multiple academic factors currently "
            "require attention."
        )

    return recommendations


def display_recommendations(
    recommendations
):
    print("\nACADEMIC RECOMMENDATIONS")
    print("=" * 58)

    for number, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"{number}. {recommendation}"
        )