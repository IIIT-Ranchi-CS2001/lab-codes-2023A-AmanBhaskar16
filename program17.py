course_code=['CS-2001','CS-2003','CS-2005','CS-2007']
course_name=['Python','COA','TOC','Algo']
mapping=list(zip(course_code,course_name))
list1=[str(x[0]+":"+x[1]) for x in mapping]
print(list1)