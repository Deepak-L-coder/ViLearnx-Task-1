# Dictionary to store subjects and grades
grades ={}

def input_grades():
    num_subjects =int(input("Enter the number of subjects:"))
    
    for i in range(num_subjects):
        subject =input(f"Enter the name of subjects {i+1}:")
        grade =float(input(f"Enter the grade for {subject}:"))
        grades[subject] = grade

def calculate_average():
    total =sum(grades.values())
    average =total/len(grades)
    return average

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_gpa(letter_grade):
    gpa_scale = {
        "A":4.0,
        "B":3.0,
        "C":2.0,
        "D":1.0,
        "F":0.0
    }
    return gpa_scale[letter_grade]

def display_results():
    average =calculate_average()
    letter_grade =get_letter_grade(average)
    gpa =get_gpa(letter_grade)
    
    print("\nResults:")
    print(f"Average Grade:{average:.2f}")
    print(f"Letter Grade:{letter_grade}")
    print(f"GPA: {gpa:.2f}")

def main():
    input_grades()
    display_results()

if __name__ == "__main__":
    main()
