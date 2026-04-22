"""
Henry B & Fox W
"""

# Add constants and functions as needed (in later labs I will not remind you to do this).
EXAM1_WEIGHT = 0.15
EXAM2_WEIGHT = 0.15
FINAL_EXAM_WEIGHT = 0.3
LAB_AND_HOMEWORK_WEIGHT = 0.3
LAB_CHECKS_AND_PARTICIPATION_WEIGHT = 0.1
A_LEVEL = 90
B_LEVEL = 80
C_LEVEL = 70
D_LEVEL = 55


def grade_needed_on_final(exam1, exam2, lab, participation, target_final_average):
    """Given a student's exam1, exam2, lab, and participation grades from CSM 2170, this function returns the grade
    needed on the final exam to have a given target as the final average for the class. All parameters are integers and
    the return value is a float. Note this function will return a value greater than 100.0 if it is not possible to make
    the target and a value less than 0.0 if any grade on the final will be above the target."""
    exam1_score = exam1 * EXAM1_WEIGHT
    exam2_score = exam2 * EXAM2_WEIGHT
    lab_score = LAB_AND_HOMEWORK_WEIGHT * lab
    participation_score = LAB_CHECKS_AND_PARTICIPATION_WEIGHT * participation
    # weights assignment scores according to the syllabus weights
    total_without_final = exam1_score + exam2_score + lab_score + participation_score
    score_needed = (target_final_average - total_without_final) / FINAL_EXAM_WEIGHT
    return score_needed


def main():
    # You may edit (and change the indentation) of the following comments as needed. They are here to just give you a
    # start on your task. Replace the pass statements with your code.
    #
    # Ask the user for their CSM 2170 grades
    user_exam1 = int(input("enter exam 1 score(whole number)): "))
    user_exam2 = int(input("enter exam 2 score(whole number): "))
    user_lab = int(input("enter lab score(whole number): "))
    user_participation = int(input("enter participation score(whole number): "))
    # Calculates needed grade for an A
    user_target_grade = A_LEVEL
    score_a = grade_needed_on_final(user_exam1, user_exam2, user_lab, user_participation, user_target_grade)
    # Calculates needed grade for a B
    user_target_grade = B_LEVEL
    score_b = grade_needed_on_final(user_exam1, user_exam2, user_lab, user_participation, user_target_grade)
    # Calculates needed grade for a C
    user_target_grade = C_LEVEL
    score_c = grade_needed_on_final(user_exam1, user_exam2, user_lab, user_participation, user_target_grade)
    # Calculates needed grad for a D
    user_target_grade = D_LEVEL
    score_d = grade_needed_on_final(user_exam1, user_exam2, user_lab, user_participation, user_target_grade)
    # Prints out needed grades in a table with error messages for impossible grades
    print("")
    print("grade | Score needed on final")
    print("------+----------------------")
    if 0 < score_a < 100:
        print(f" A    | {score_a:.2f}")
    else:
        print(" A    | Not Possible")
    if 0 < score_b < 100:
        print(f" B    | {score_b:.2f}")
    else:
        print(" B    | Not Possible")
    if 0 < score_b < 100:
        print(f" C    | {score_c:.2f}")
    else:
        print(" C    | Not Possible")
    if 0 < score_d < 100:
        print(f" D    | {score_d:.2f}")
    else:
        print(" D    | Not Possible")

    # Use grade_needed_on_final to find what grades are needed to earn: A, B, C, and D  in the class. Print the results
    # as a nicely formatted table.
    pass


# ********************************************************************************************************************
# Do not edit code below this point.
# ********************************************************************************************************************
if __name__ == "__main__":
    main()
