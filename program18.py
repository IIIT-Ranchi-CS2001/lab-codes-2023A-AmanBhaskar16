s1 = set(input("Enter the names of singers of class: ").split())
s2 = set(input("Enter the names of dancers of class: ").split())
print(f"Artists of the class : {s1 | s2}")
print(f"ALl rounders of the class : {s1 & s2}")
print(f"Singers but not dancers : {s1 - s2}")
print(f"Dancers but not singers : {s2 - s1}")
print(f"Dancers but not singers cum singers but not dancers : {s1^s2}")