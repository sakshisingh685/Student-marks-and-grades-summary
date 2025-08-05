# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

# Input number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# List to store subject names
subjects = []
for i in range(num_subjects):
    subject = input(f"Enter name of subject {i+1}: ")
    subjects.append(subject)

# Dictionary to store student records
students = {}

# Get marks for each student
for i in range(num_students):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    total = 0
    
    for subject in subjects:
        mark = float(input(f"Enter marks in {subject}: "))
        marks.append(mark)
        total += mark

    percentage = total / num_subjects
    grade = calculate_grade(percentage)
    
    students[name] = {
        'Marks': marks,
        'Total': total,
        'Percentage': percentage,
        'Grade': grade
    }

# Display summary
print("\n===== Student Marksheet Summary =====")
for name, data in students.items():
    print(f"\nName: {name}")
    for i in range(num_subjects):
        print(f"  {subjects[i]}: {data['Marks'][i]}")
    print(f"  Total: {data['Total']}")
    print(f"  Percentage: {data['Percentage']:.2f}%")
    print(f"  Grade: {data['Grade']}")

