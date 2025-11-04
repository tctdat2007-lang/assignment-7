names = set()
while True:
    name = input("Enter a name (empty to stop): ").strip()
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("You entered the following names:")
for n in names:
    print(n)
