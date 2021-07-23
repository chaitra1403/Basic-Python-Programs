from oper import *
a=over()
b=over()
a.getdata()
b.getdata()
print(a.alist)
print(b.alist)
while True:
	print("\n1.add\n2.sub\n3.mul\n4.div\n5.floordiv")
	ch=int(input("enter the choice"))
	if ch==1:
		print(a+b)
	elif ch==2:
		print(a-b)
	elif ch==3:
		print(a*b)
	elif ch==4:
		print(a/b)
	elif ch==5:
		print(a//b)
		
