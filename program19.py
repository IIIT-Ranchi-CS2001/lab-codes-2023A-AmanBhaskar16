
t1 = tuple([int(x) for x in input("Enter multiple integers separated by spaces: ").split()])
t2 = tuple([int(y) for y in input("Enter multiple integers separated by spaces: ").split()])

tup = tuple(zip(t1,t2))
dist = 0
print(tup)
for i in tup:
    dist = dist + ((i[0] - i[1])**2)
print("Euclidean distance : ")
print(dist**0.5)