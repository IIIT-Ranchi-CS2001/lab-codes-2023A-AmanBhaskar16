import math

a = 3
b =4
c =5

discriminant = b**2 - 4*a*c

if discriminant > 0:
  q1 = (-b + math.sqrt(discriminant)) / (2*a)
  q2 = (-b - math.sqrt(discriminant)) / (2*a)
  print("the roots are : ",q1," and ",q2)
elif discriminant == 0: 
  q = -b / (2*a)
  print("The equal roots are : ",q)
else:
  real_part = -b/(2*a)
  imaginary_part = math.sqrt(-discriminant)/(2*a)
  print(real_part,"+",imaginary_part)
  print(real_part,"-",imaginary_part)


