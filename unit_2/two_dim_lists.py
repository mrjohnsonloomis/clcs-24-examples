'''
Demonstrates the effective use of 2 dimensional lists
'''
def add_or_update_student(grade_sheet: list[list[str]], student_name: str, grades: list[int]) -> None:
    # Convert grades to strings
    grades_str = [str(grade) for grade in grades]

    for student in grade_sheet:
        if student[0] == student_name:
            student[1:] = grades_str
            return
    grade_sheet.append([student_name] + grades_str)

def calculate_average(grade_sheet: list[list[str]], student_name: str) -> float:
    for student in grade_sheet[1:]:  # Skip header row
        if student[0] == student_name:
            # Convert grade strings to integers for calculation
            numeric_grades = [int(grade) for grade in student[1:]]
            average = sum(numeric_grades) / len(numeric_grades)
            return average
    return 0.0  # Return 0.0 if student is not found

def display_grade_sheet(grade_sheet: list[list[str]]) -> None:
    for row in grade_sheet:
        for item in row:
            print(f"{item}\t", end="")
        print()
    print()

# Pre-populated grade sheet
grade_sheet = [
    ["Name", "Assignment 1", "Assignment 2", "Final Exam"],
    ["Alice", "85", "90", "95"],
    ["Bob", "75", "80", "85"],
    ["Charlie", "100", "85", "90"]
]

# Display the grade sheet
print("Grade Sheet:")
display_grade_sheet(grade_sheet)

# Example usage of add_or_update_student and calculate_average
add_or_update_student(grade_sheet, "Diana", [88, 92, 87])
print("Updated Grade Sheet:")
display_grade_sheet(grade_sheet)

student_name = "Alice"
average = calculate_average(grade_sheet, student_name)
if average > 0:
    print(f"Average for {student_name}: {average}")
else:
    print(f"Student {student_name} not found.")
