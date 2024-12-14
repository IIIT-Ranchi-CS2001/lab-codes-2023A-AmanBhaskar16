name = ['amit','rahul','aman']
id = [1001,1002,1003]
s_list = ['abc','xyz','jkl']

new = zip(name,id,s_list)
comb_zip = list(new)
# print(comb_zip)

comb = []
for i in range(len(name)):
    comb.append((name[i], id[i],s_list[i]))
print("zipping original inputs : ")
print(comb)

sorted_comb  = sorted(comb_zip)
print("After applying sorted function : ")
print(sorted_comb)

n = len(comb)
for i in range(n):
    for j in range(0,n-i-1):
        if(comb[j]>comb[j+1]):
            comb[j],comb[j+1] = comb[j+1],comb[j]
print("Without using sorted function : ")
print(comb)