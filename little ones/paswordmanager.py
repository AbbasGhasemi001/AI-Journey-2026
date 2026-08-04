while True:

    print("\n===== Password Manager =====")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter your answer: ")

    if choice == "1":

        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        with open("passwords.txt", "a") as file:
            file.write(
                f"{website},{username},{password}\n"
            )

        print("Account added successfully!")



    elif choice == "2":

        try:

            with open("passwords.txt", "r") as file:

                print("\n===== Accounts =====")

                for line in file:

                    website, username, password = (
                        line.strip().split(",")
                    )

                    print(
                        f"\nWebsite: {website}"
                    )

                    print(
                        f"Username: {username}"
                    )

                    print(
                        f"Password: {password}"
                    )

                    print("-------------------")

        except FileNotFoundError:
            print("No accounts found!")



    elif choice == "3":

        search = input(
            "Enter website: "
        )

        found = False

        try:

            with open(
                "passwords.txt",
                "r"
            ) as file:

                for line in file:

                    website, username, password = (
                        line.strip().split(",")
                    )

                    if (
                        search.lower()
                        in website.lower()
                    ):

                        print("\nFound!")

                        print(
                            f"Website: {website}"
                        )

                        print(
                            f"Username: {username}"
                        )

                        print(
                            f"Password: {password}"
                        )

                        found = True

            if found == False:
                print(
                    "Account not found"
                )

        except FileNotFoundError:
            print(
                "No accounts file found!"
            )



    elif choice == "4":

        try:

            with open(
                "passwords.txt",
                "r"
            ) as file:

                accounts = file.readlines()

            delete_name = input(
                "Enter website to delete: "
            )

            with open(
                "passwords.txt",
                "w"
            ) as file:

                found = False

                for line in accounts:

                    website, username, password = (
                        line.strip().split(",")
                    )

                    if (
                        delete_name.lower()
                        != website.lower()
                    ):

                        file.write(line)

                    else:
                        found = True

                if found:
                    print(
                        "Account deleted!"
                    )
                else:
                    print(
                        "Account not found!"
                    )

        except FileNotFoundError:
            print(
                "No accounts file found!"
            )



    elif choice == "5":

        print("Goodbye 👋")
        break


    else:

        print(
            "Invalid choice!"
        )