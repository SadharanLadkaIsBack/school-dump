import csv
import os

# Function to create and add data to the CSV file
def add_data(file_name):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        writer.writerow([roll_no, name, marks])
        print("Record added successfully.")

# Function to display all records from the CSV file
def display_data(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            print("\nStudent Records:")
            print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10}")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10}")
    except FileNotFoundError:
        print("No records found.")

# Function to search for a record by roll number in the CSV file
def search_record(file_name, roll_no):
    found = False
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == roll_no:
                    print(f"Record Found: Roll No: {row[0]}, Name: {row[1]}, Marks: {row[2]}")
                    found = True
                    break
        if not found:
            print("Record not found.")
    except FileNotFoundError:
        print("No records found.")

# Main menu to perform operations
def main():
    file_name = "students.csv"
    
    while True:
        print("\n--- Student Records Menu ---")
        print("1. Add Data")
        print("2. Display Data")
        print("3. Search Record")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_data(file_name)
        elif choice == 2:
            display_data(file_name)
        elif choice == 3:
            roll_no = input("Enter Roll No to search: ")
            search_record(file_name, roll_no)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
