"""
computes final grade in class
Henry B & Fox W
"""

# Add constants and functions as needed (in later labs I will not remind you to do this).
EXAM1_WEIGHT = 0.15
EXAM2_WEIGHT = 0.15
FINAL_EXAM_WEIGHT = 0.3
LAB_AND_HOMEWORK_WEIGHT = 0.3
LAB_CHECKS_AND_PARTICIPATION_WEIGHT = 0.1


def final_average(exam1, exam2, final, lab, participation):
    """Given a student's exam1, exam2, final, lab, and participation grades from CSM 2170, this function returns their
    final average as a float."""
    exams = exam1 * EXAM1_WEIGHT + exam2 * EXAM2_WEIGHT + final * FINAL_EXAM_WEIGHT
    labs = lab * LAB_AND_HOMEWORK_WEIGHT + participation * LAB_CHECKS_AND_PARTICIPATION_WEIGHT
    return exams + labs


def letter_grade(score):
    """Given a grade (score) from CSM 2170, this function returns the corresponding letter grade as a string (one
    uppercase letter)."""
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 55 <= score < 70:
        return "D"
    elif score < 55:
        return "F"


def main():
    # Ask the user for their CSM 2170 grades
    user_exam1 = float(input("enter exam 1 score rounded to 2 decimal points: "))
    user_exam2 = float(input("enter exam 2 score rounded to 2 decimal points: "))
    user_final_exam = float(input("enter final exam score rounded to 2 decimal points: "))
    user_lab = float(input("enter lab score rounded to 2 decimal points: "))
    user_participation = float(input("enter participation score rounded to 2 decimal points: "))
    # determines user's final number grade from the entered values
    user_score = final_average(user_exam1, user_exam2, user_final_exam, user_lab, user_participation)
    # prints the letter earned
    print(f"Letter grade: {str(letter_grade(user_score))}")
    # returns the grades' number value
    print(f"{user_score:.2f}")


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
