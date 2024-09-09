import math;

a = float(input("Enter 1st side length : "))
b = float(input("Enter 2nd side length: "))
c = float(input("Enter 3rd side length : "))

x = a+b+c
print("The perimeter of the triangle is: ")
print(x)

s = x/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is :")
print(area)
alpha= math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
beta = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
gamma = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))
print("The angles are :")
print(alpha)
print(beta)
print(gamma)
