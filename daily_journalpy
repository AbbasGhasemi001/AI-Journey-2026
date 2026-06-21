while True:

    note = input("Write your day's note: ")

    with open("journal.txt", "a") as file:
        file.write(note + "\n")

    choice = input("Add another? (y/n): ")

    if choice.lower() == "n":
        break


print("\nYour Notes:\n")

with open("journal.txt", "r") as file:
    print(file.read())