
n = int(input("Number of Fibonacci Series to be Printed: "))

a, b = 0, 1
print(a, b, end=' ')

i = 0
while (i < n-2):
    c = a + b
    
    print(c, end=' ')
    a = b
    b = c
    i = i + 1