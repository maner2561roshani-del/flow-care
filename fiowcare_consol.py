import csv

while True:

    print("\n========== FLOW CARE ==========")
    print("1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        last_period = input("Enter Last Period Date (DD-MM-YYYY): ")

        with open("flowcare_dataset.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, last_period])

        print("Data Saved Successfully!")

    elif choice == "2":
        with open("flowcare_dataset.csv", "r") as file:
            reader = csv.reader(file)

            print("\n----- Records -----")
            for row in reader:
                print(row)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        