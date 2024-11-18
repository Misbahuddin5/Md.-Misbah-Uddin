class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}"

class StudentInformationSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        """ Add a new student to the system. """
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        grade = input("Enter Student Grade: ")
        
        # Create a new Student object and add it to the dictionary
        student = Student(student_id, name, grade)
        self.students[student_id] = student
        print(f"Student {name} added successfully!\n")

    def view_students(self):
        """ Display all student records. """
        if not self.students:
            print("No students in the system.\n")
        else:
            print("\n--- Student Records ---")
            for student in self.students.values():
                print(student)
            print()

    def search_student(self):
        """ Search for a student by ID. """
        student_id = input("Enter Student ID to search: ")
        student = self.students.get(student_id)
        
        if student:
            print("\nStudent Found:")
            print(student)
        else:
            print("Student not found!\n")

    def update_student(self):
        """ Update student information. """
        student_id = input("Enter Student ID to update: ")
        student = self.students.get(student_id)
        
        if student:
            print(f"Current Info: {student}")
            name = input("Enter new Name (leave blank to keep current): ")
            grade = input("Enter new Grade (leave blank to keep current): ")
            
            # Update student info if new data is provided
            if name:
                student.name = name
            if grade:
                student.grade = grade
            print("Student information updated successfully!\n")
        else:
            print("Student not found!\n")

    def delete_student(self):
        """ Delete a student record from the system. """
        student_id = input("Enter Student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted successfully!\n")
        else:
            print("Student not found!\n")

    def main_menu(self):
        """ Display the main menu and handle user input. """
        while True:
            print("----- Student Information System -----")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student by ID")
            print("4. Update Student Information")
            print("5. Delete Student")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    system = StudentInformationSystem()
    system.main_menu()
