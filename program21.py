s=input("enter the string:")
dict={}
t=s.split()
for i in t:
    for j in i:
        if(j not in dict):
            dict[j]=1
        else:
            dict[j]+=1
print(dict) 