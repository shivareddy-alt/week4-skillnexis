
import pandas as pd
from pathlib import Path

# Get the folder where this Python file is saved
folder = Path(__file__).parent
input_file = folder / "employees.csv"
output_file = folder / "high_salary_employees.csv"

if not input_file.exists():
    data = {
        "EmployeeID": [101, 102, 103, 104, 105, 106],
        "Name": ["Ravi", "Sita", "Arun", "Priya", "Kiran", "Divya"],
        "Department": [
            "IT", "HR", "IT", "Finance", "HR", "Finance"
        ],
        "Salary": [45000, 35000, 60000, 50000, 40000, 70000]
    }

    df = pd.DataFrame(data)
    df.to_csv(input_file, index=False)
    print("Sample employee dataset created.")

# Load employee data from CSV
df = pd.read_csv(input_file)

while True:
    print("\n===== EMPLOYEE DATA ANALYSIS =====")
    print("1. Display all employees")
    print("2. Calculate average salary")
    print("3. Count employees by department")
    print("4. Filter employees by salary")
    print("5. Export filtered employees to CSV")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        print("\nEmployee Details:")
        print(df.to_string(index=False))

    elif choice == "2":
        average_salary = df["Salary"].mean()
        print(f"Average Salary: ₹{average_salary:.2f}")

    elif choice == "3":
        print("\nEmployees in Each Department:")
        print(df["Department"].value_counts().to_string())

    elif choice == "4":
        try:
            threshold = float(input("Enter minimum salary: ₹"))
            filtered_df = df[df["Salary"] > threshold]

            if filtered_df.empty:
                print("No employees found above this salary.")
            else:
                print("\nEmployees Above Salary Threshold:")
                print(filtered_df.to_string(index=False))

        except ValueError:
            print("Please enter a valid salary.")

    elif choice == "5":
        try:
            threshold = float(input("Enter salary threshold: ₹"))
            filtered_df = df[df["Salary"] > threshold]

            filtered_df.to_csv(output_file, index=False)
            print("Filtered employee data exported successfully.")
            print("File location:", output_file)

        except ValueError:
            print("Please enter a valid salary.")

    elif choice == "6":
        print("Thank you for using Employee Data Analysis!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
