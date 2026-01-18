def add_student(students, name, grades):
    """Add a student with their grades to the dictionary."""
    students[name] = grades
    return students

def calculate_average(grades):
    """Calculate the average grade for a student."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(average):
    """Convert numeric average to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def display_student_info(students, name):
    """Display detailed information for a specific student."""
    if name in students:
        grades = students[name]
        avg = calculate_average(grades)
        letter = get_letter_grade(avg)
        print(f"Student: {name}")
        print(f"Grades: {grades}")
        print(f"Average: {avg:.2f}")
        print(f"Letter Grade: {letter}")
    else:
        print(f"Student {name} not found.")

def find_top_student(students):
    """Find the student with the highest average grade."""
    if not students:
        return None
    
    top_student = None
    highest_avg = -1
    
    for name, grades in students.items():
        avg = calculate_average(grades)
        if avg > highest_avg:
            highest_avg = avg
            top_student = name
    
    return top_student, highest_avg

def main():
    students = {}
    
    # Add students
    add_student(students, "Alice", [85, 92, 78, 96])
    add_student(students, "Bob", [76, 81, 72, 85])
    add_student(students, "Charlie", [95, 89, 92, 88])
    
    # Display all students
    for name in students:
        display_student_info(students, name)
        print("-" * 20)
    
    # Find top student
    top_name, top_avg = find_top_student(students)
    print(f"Top Student: {top_name} with average {top_avg:.2f}")

main()