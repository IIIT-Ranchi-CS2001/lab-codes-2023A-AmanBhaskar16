
k=input("enter the names: ").split()
l1=[i for i in k]
l2 = [int(x) for x in input("Enter customer ID: ").split()]
l3 = [int(x) for x in input("Enter shopping points : ").split()]
l=zip(l1,l2,l3)
l=list(l)
print(sorted(l,key=lambda x:x[2]))