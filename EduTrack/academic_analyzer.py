PROJECT_GRADE_SCALE = [
    (90, 10, "S"),
    (80, 9, "A"),
    (70, 8, "B"),
    (60, 7, "C"),
    (50, 6, "D"),
    (40, 5, "E"),
    (0, 0, "F")
]


def get_grade(mark):
    for minimum, grade_point, grade in PROJECT_GRADE_SCALE:
        if mark >= minimum:
            return grade, grade_point

    return "F", 0


def analyze_performance(academic):
    results = {}

    total_points = 0
    total_credits = 0

    for subject, mark in academic["marks"].items():
        grade, grade_point = get_grade(mark)
        credits = academic["credits"][subject]

        results[subject] = {
            "marks": mark,
            "grade": grade,
            "grade_point": grade_point,
            "credits": credits
        }

        total_points += grade_point * credits
        total_credits += credits

    if total_credits > 0:
        sgpa = total_points / total_credits
    else:
        sgpa = 0

    strong_subjects = []
    weak_subjects = []

    for subject, result in results.items():
        if result["grade_point"] >= 9:
            strong_subjects.append(subject)

        elif result["grade_point"] <= 6:
            weak_subjects.append(subject)

    ranked_subjects = sorted(
        results.items(),
        key=lambda item: item[1]["marks"],
        reverse=True
    )

    return {
        "subjects": results,
        "sgpa": sgpa,
        "strong_subjects": strong_subjects,
        "weak_subjects": weak_subjects,
        "ranked_subjects": ranked_subjects
    }


def calculate_current_cgpa(academic, sgpa):
    semester = int(academic["semester"])

    current_credits = sum(
        academic["credits"].values()
    )

    if semester == 1:
        return sgpa

    previous_cgpa = academic["previous_cgpa"]
    previous_credits = academic["previous_credits"]

    total_credits = (
        previous_credits + current_credits
    )

    if total_credits == 0:
        return sgpa

    return (
        (previous_cgpa * previous_credits)
        + (sgpa * current_credits)
    ) / total_credits