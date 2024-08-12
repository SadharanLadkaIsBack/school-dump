import pickle
import os

# Function to add a student record to the binary file
def add_data(file_name):
    with open(file_name, 'ab') as file:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = {'roll_no': roll_no, 'name': name, 'marks': marks}
        pickle.dump(student, file)
        print("Record added successfully.")

# Function to display all student records from the binary file
def display_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            print("\nStudent Records:")
            while True:
                try:
                    student = pickle.load(file)
                    print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found.")

# Function to search for a student record by roll number
def search_record(file_name, roll_no):
    found = False
    try:
        with open(file_name, 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['roll_no'] == roll_no:
                        print(f"Record Found: Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
                        found = True
                        break
                except EOFError:
                    break
        if not found:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Function to update marks of a student by roll number
def update_marks(file_name, roll_no, new_marks):
    students = []
    updated = False
    try:
        with open(file_name, 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['roll_no'] == roll_no:
                        student['marks'] = new_marks
                        updated = True
                    students.append(student)
                except EOFError:
                    break

        if updated:
            with open(file_name, 'wb') as file:
                for student in students:
                    pickle.dump(student, file)
            print("Marks updated successfully.")
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Function to delete a student record by roll number
def delete_record(file_name, roll_no):
    students = []
    deleted = False
    try:
        with open(file_name, 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['roll_no'] != roll_no:
                        students.append(student)
                    else:
                        deleted = True
                except EOFError:
                    break

        if deleted:
            with open(file_name, 'wb') as file:
                for student in students:
                    pickle.dump(student, file)
            print("Record deleted successfully.")
        else:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Main menu to perform operations
def main():
    file_name = "students.dat"
    
    while True:
        print("\n--- Student Records Menu ---")
        print("1. Add Data")
        print("2. Display Data")
        print("3. Search Record")
        print("4. Update Marks")
        print("5. Delete Record")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_data(file_name)
        elif choice == 2:
            display_data(file_name)
        elif choice == 3:
            roll_no = int(input("Enter Roll No to search: "))
            search_record(file_name, roll_no)
        elif choice == 4:
            roll_no = int(input("Enter Roll No to update marks: "))
            new_marks = float(input("Enter new marks: "))
            update_marks(file_name, roll_no, new_marks)
        elif choice == 5:
            roll_no = int(input("Enter Roll No to delete: "))
            delete_record(file_name, roll_no)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
