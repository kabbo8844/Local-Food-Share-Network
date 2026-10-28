import os

food_file = "food_data.txt"
volunteer_file = "volunteer_data.txt"
log_file = "distribution_log.txt"


def add_food():
    print("\n--- Donate Food ---")

    donor = input("Enter donor name: ")
    location = input("Enter location: ")
    food_name = input("Enter food name: ")
    quantity = input("Enter quantity (e.g. 20 packets): ")
    expiry = input("How many hours will the food stay good? ")

    food_id = 1

    if os.path.exists(food_file):
        with open(food_file, "r") as file:
            lines = file.readlines()
            food_id = len(lines) + 1

    food_info = (
        str(food_id) + "|" +
        donor + "|" +
        location.lower() + "|" +
        food_name + "|" +
        quantity + "|" +
        expiry + "|Available\n"
    )

    with open(food_file, "a") as file:
        file.write(food_info)

    print("\nFood donation added successfully!")


def add_volunteer():
    print("\n--- Register Volunteer ---")

    name = input("Enter volunteer name: ")
    location = input("Enter volunteer location: ")
    phone = input("Enter contact number: ")

    volunteer_info = (
        name + "|" +
        location.lower() + "|" +
        phone + "\n"
    )

    with open(volunteer_file, "a") as file:
        file.write(volunteer_info)

    print("\nVolunteer registered successfully!")


def show_food():
    print("\n--- Available Food Donations ---")

    if not os.path.exists(food_file):
        print("No food donation found.")
        return

    found = False

    with open(food_file, "r") as file:
        for line in file:
            data = line.strip().split("|")

            if len(data) == 7 and data[6] == "Available":
                print("\nFood ID:", data[0])
                print("Donor:", data[1])
                print("Location:", data[2])
                print("Food:", data[3])
                print("Quantity:", data[4])
                print("Expiry:", data[5], "hours")
                found = True

    if not found:
        print("No available food donations.")


def find_volunteer(food_location):
    if not os.path.exists(volunteer_file):
        return None

    with open(volunteer_file, "r") as file:
        for line in file:
            data = line.strip().split("|")

            if len(data) == 3 and data[1] == food_location:
                return data

    return None


def match_food():
    print("\n--- Match Food With Volunteer ---")

    if not os.path.exists(food_file):
        print("No food donations found.")
        return

    with open(food_file, "r") as file:
        foods = file.readlines()

    found = False

    for line in foods:
        data = line.strip().split("|")

        if len(data) == 7 and data[6] == "Available":
            volunteer = find_volunteer(data[2])

            if volunteer is not None:
                print("\nFood ID:", data[0])
                print("Food:", data[3])
                print("Location:", data[2])
                print("Volunteer:", volunteer[0])
                print("Contact:", volunteer[2])
                print("Expiry:", data[5], "hours")
                found = True

    if not found:
        print("No matching volunteer found in the same area.")


def distribute_food():
    print("\n--- Distribute Food ---")

    show_food()

    food_id = input("\nEnter Food ID to distribute: ")

    if not os.path.exists(food_file):
        print("No food donations found.")
        return

    with open(food_file, "r") as file:
        foods = file.readlines()

    updated_foods = []
    selected_food = None

    for line in foods:
        data = line.strip().split("|")

        if (
            len(data) == 7
            and data[0] == food_id
            and data[6] == "Available"
        ):
            volunteer = find_volunteer(data[2])

            if volunteer is not None:
                data[6] = "Distributed"
                selected_food = data

                with open(log_file, "a") as log:
                    log.write(
                        "Food ID: " + data[0] +
                        " | Food: " + data[3] +
                        " | Quantity: " + data[4] +
                        " | Location: " + data[2] +
                        " | Volunteer: " + volunteer[0] +
                        " | Status: Distributed\n"
                    )

                print("\nFood marked as distributed.")
                print("Volunteer:", volunteer[0])
            else:
                print("No volunteer found in this area.")

        updated_foods.append("|".join(data) + "\n")

    with open(food_file, "w") as file:
        file.writelines(updated_foods)

    if selected_food is None:
        print("Food was not distributed. Check the Food ID and volunteer list.")


def show_log():
    print("\n--- Distribution Log ---")

    if not os.path.exists(log_file):
        print("No distribution record found.")
        return

    with open(log_file, "r") as file:
        content = file.read()

    if content:
        print(content)
    else:
        print("No distribution record found.")


def main():
    while True:
        print("\n==============================")
        print(" LOCAL FOOD SHARE NETWORK")
        print("==============================")
        print("1. Donate Food")
        print("2. Register Volunteer")
        print("3. View Available Food")
        print("4. Match Food With Volunteer")
        print("5. Mark Food As Distributed")
        print("6. View Distribution Log")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_food()

        elif choice == "2":
            add_volunteer()

        elif choice == "3":
            show_food()

        elif choice == "4":
            match_food()

        elif choice == "5":
            distribute_food()

        elif choice == "6":
            show_log()

        elif choice == "7":
            print("Thank you for using Food Share Network!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
