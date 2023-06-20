"""
Author: Aung Zin Paing
Dean's List or Honor Roll checker
This program will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
"""
while True:
    stu_last_name = input("Enter student's last name or ZZZ to quit: ")
    if stu_last_name == "ZZZ":
        print("Quiting program...")
        break
    stu_first_name = input("Enter student's first name: ")
    GPA = float(input("Enter student's GPA: "))

    if GPA > 4.0 or GPA < 0.0:
        print("Invalid Entry")
    elif GPA >= 3.5:
        print("You made it into the Dean's List")
    elif GPA >= 3.25:
        print("You made it into the Honor Roll")
    else:
        print("You didn't made it into Dean's list nor Honor Roll")
