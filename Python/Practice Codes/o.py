
d = {

    "Wizard": "1"

}

classSelection = input("Enter your class: ")
classSelection1 = input("Enter your class: ")

if classSelection == "1":
    print("1-1")

if classSelection1 == "1":
    print("1-2")

if classSelection == classSelection1:
    while(classSelection == classSelection1):
        print("")
        print('duplicated values, select new class.')
        classSelection1 = input("Enter your class: ")

print(classSelection)
print(classSelection1)

