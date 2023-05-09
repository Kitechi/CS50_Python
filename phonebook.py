import csv
with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
    file.close()
    
# people = dict() or people = {} same thing for declaring dictionary
# people = {
#     "Salah": "010-2875-0390",
#     "Sarim": "010-7275-4563"
# }

# name = input("Name: ")
# if name in people:
#     print(f"Number: {people[name]}")
    