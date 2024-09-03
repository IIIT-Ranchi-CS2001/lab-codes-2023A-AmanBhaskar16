a = input("Enter name : ");
b = int(input("Enter roll no. : "));
c = int(input("Enter the marks scored : "));
print("Name : ",a);
print("Roll Number : ",b);
print("marks : ",c);
if(c>=90):
  print("Grade Point :",10);
  print("Remark : OUTSTANDING");
elif(c>=80):
  print("Grade Point :",9);
  print("Remark : VERY GOOD");
elif(c>=70):
  print("Grade Point :",8);
  print("Remark : GOOD");
elif(c>=60):
  print("Grade Point :",7);
  print("Remark : AVERAGE");
elif(c>=80):
  print("Grade Point :",6);
  print("Remark : PASS");
else:
  print("Grade Point :",0);
  print("Remark : FAIL");
