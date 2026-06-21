while True:
    print ("\n Enter  your information please !")
    name= input("Enter name :")
    age = input("Enter your age :")
    with open ("users.txt","a")as file :
        file.write(f"{name}, {age}\n")
    choice = str(input("add again ?y/n"))
    if choice.lower()=="n":
        break
print ("\nusers information")
with open ("users.txt","r") as file :
    print(file.read())

