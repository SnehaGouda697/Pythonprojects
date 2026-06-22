#Dictionary used
#conditional statements
#function def

"""
add
update
delete
view
exit

"""


# Initializing the dictionary
student_grade = {}

# Add new student
def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with grade {grade}")

# Update student
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print(f"{name} is not found")

# Delete student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} successfully deleted")
    else:
        print(f"{name} is not found")

# View students
def display_student():
    if student_grade:
        print("\nStudent Records:")
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added")

# Main logic
def main():
    while True:
        print("\n<<< Student Management System >>>")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        choice = int(input("Enter your choice = "))

        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter the student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter the new grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_student()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

# Run the program
main()
            

    
    
            
            
        
        
        






    


