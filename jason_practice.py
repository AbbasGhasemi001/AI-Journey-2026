import json

book = {
    "name":"Atomic Habits",
    "author":"James Clear",
    "pages":320
}

with open("book.json","w") as file:
    json.dump(book,file,indent=4)

print("Saved!")

with open("book.json","r") as file:
    data = json.load(file)

print(data["name"])