students = []

while True:
    print("\n===== STUDENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Student name: ")
        grade = input("Grade: ")
        students.append((name, grade))
        print("Student added successfully!")

    elif choice == "2":
        print("\n--- Student List ---")
        if len(students) == 0:
            print("No students yet.")
        else:
            for s in students:
                print("Name:", s[0], "| Grade:", s[1])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
