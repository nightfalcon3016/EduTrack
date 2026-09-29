ATTENDANCE_THRESHOLD = 75
NINE_POINT_THRESHOLD = 9


def calculate_attendance(attended, total):
    if total == 0:
        return 0

    return (attended / total) * 100


def classes_needed_for_eligibility(attended, total):
    attendance = calculate_attendance(
        attended,
        total
    )

    if attendance >= ATTENDANCE_THRESHOLD:
        return 0

    required = 0

    while calculate_attendance(
        attended + required,
        total + required
    ) < ATTENDANCE_THRESHOLD:
        required += 1

    return required


def maximum_safe_absences(attended, total):
    absences = 0

    while calculate_attendance(
        attended,
        total + absences + 1
    ) >= ATTENDANCE_THRESHOLD:
        absences += 1

    return absences


def analyze_attendance(academic, current_cgpa):
    attended = academic["classes_attended"]
    total = academic["total_classes"]

    attendance = calculate_attendance(
        attended,
        total
    )

    semester = int(academic["semester"])
    backlogs = academic["backlogs"]

    exemption = (
        semester > 1
        and current_cgpa >= NINE_POINT_THRESHOLD
        and not backlogs
    )

    if exemption:
        status = "EXEMPT FROM MINIMUM ATTENDANCE REQUIREMENT"
        eligible = True

    elif attendance >= ATTENDANCE_THRESHOLD:
        status = "ELIGIBLE"
        eligible = True

    else:
        status = "DEBARRED"
        eligible = False

    return {
        "attendance": attendance,
        "threshold": ATTENDANCE_THRESHOLD,
        "status": status,
        "eligible": eligible,
        "exemption": exemption,
        "classes_needed": classes_needed_for_eligibility(
            attended,
            total
        ),
        "safe_absences": maximum_safe_absences(
            attended,
            total
        )
    }