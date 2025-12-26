import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File name
FILE_NAME = "attendance.csv"
# Create file if not exists
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Roll_No", "Name", "Date", "Status"])
    df.to_csv(FILE_NAME, index=False)



# Function to mark attendance
def mark_attendance():
    roll_no = input("Enter ID no.: ")
    


    
    name = input("Enter Name: ")
    date = input("Enter Date (DD-MM-YYYY): ")

    # Basic date validation
    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        print("Invalid date format! Use DD-MM-YYYY\n")
        return

    day, month, year = date.split('-')

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("Date should contain only numbers\n")
        return

    day = int(day)
    month = int(month)
    year = int(year)

    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900:
        print("Invalid date values!\n")
        return

    status = int(input("Enter Status (1 = Present, 0 = Absent): "))

    new_data = pd.DataFrame([[roll_no, name, date, status]],
                            columns=["Roll_No", "Name", "Date", "Status"])
    

    new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)
    print("Attendance Recorded Successfully!\n")



# Function to calculate attendance percentage
def attendance_percentage():
    df = pd.read_csv(FILE_NAME)

    roll_no = input("Enter ID no. : ")
    name = input("Enter Name: ")

    # Convert to string for safe comparison
    df["Roll_No"] = df["Roll_No"].astype(str)
    df["Name"] = df["Name"].astype(str)

    student_data = df[(df["Roll_No"] == roll_no) & (df["Name"] == name)]

    if student_data.empty:
        print("No record found!")
        return

    total_days = len(student_data)
    present_days = student_data["Status"].sum()
    percentage = (present_days / total_days) * 100

    print(f"Total Days: {total_days}")
    print(f"Present Days: {present_days}")
    print(f"Attendance Percentage: {percentage:.2f}%\n")



# Function to show attendance summary
def attendance_summary():
    df = pd.read_csv(FILE_NAME)
    summary = df.groupby("Name")["Status"].mean() * 100
    print("\nAttendance Summary (%):")
    print(summary)
    print()


# Function to visualize attendance
def visualize_attendance():
    df = pd.read_csv(FILE_NAME)

    roll_no = input("Enter ID no. : ")
    name = input("Enter Name: ")

    # Convert columns to string for safe comparison
    df["Roll_No"] = df["Roll_No"].astype(str)
    df["Name"] = df["Name"].astype(str)

    # Filter using both Roll_No and Name
    student_data = df[(df["Roll_No"] == roll_no) & (df["Name"] == name)]

    if student_data.empty:
        print("No data found!")
        return

    present = student_data["Status"].sum()
    absent = len(student_data) - present

    labels = ["Present", "Absent"]
    values = [present, absent]

    plt.figure(figsize=(10,6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Attendance Summary\n{name} (Roll No: {roll_no})")
    plt.show()




# Menu
while True:
    print("===== Attendance Management System =====")
    print("1. Mark Attendance")
    print("2. Calculate Attendance Percentage")
    print("3. Attendance Summary")
    print("4. Visualize Attendance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mark_attendance()
    elif choice == 2:
        attendance_percentage()
    elif choice == 3:
        attendance_summary()
    elif choice == 4:
        visualize_attendance()
    elif choice == 5:
        print("Exiting System...")
        break
    else:
        print("Invalid Choice!\n")
