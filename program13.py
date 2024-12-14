str_input = input("Enter a string: ")

for char in str_input:
    if not char.isalnum():
        print(False)
        break
else:
    print(True)