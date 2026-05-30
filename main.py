students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student name: ")
        grade = input("Grade: ")
        students.append((name, grade))

    elif choice == "2":
        for s in students:
            print(s)

    elif choice == "3":
        break
