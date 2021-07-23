while True:
	print("operations of string and tuples")
	print("--"*50)
	print("\n1.string\n2.tuples")
	print("--"*50)
	ch=int(input("enter your choice"))
	if ch==1:
		f=1
		print("operation on string")
		print("--"*50)
		str1=input("enter the string")
		while f:
			print("\n1.concate\n2.uppercase\n3.lowercase\n4.rang slicing\n5.reverse\n6.find \n7.replace\n8.slicing\n9.count\n10.repetation\n11.member\n12.iteration\n")
			print("---"*50)
			ch=int(input("enter your choice"))
			print("---"*50)
			if ch==1:
				str2=input("enter the string to concate with")
				print(str1+str2)
			elif ch==2:
				print(str1.upper())
			elif ch==3:
				print(str1.lower())
			elif ch==4:
				print(str1[0:4])
			elif ch==5:
				print(str1[::-1])
			elif ch==6:
				x=input("enter the word to find")
				print(str1.find(x))
			elif ch==7:
				x=input("enter the word to find")
				y=input("enter the word to replace")
				print(str1.replace(x,y))
			elif ch==8:
				print(str1[2])
			elif ch==9:
				print(len(str1))
			elif ch==10:
				x=int(input("how many times you want to repete"))
				print(str1*x)
			elif ch==11:
				x=input("enter the member")
				print(x in str1)
			elif ch==12:
				for i in str1:
					print(i)
			else:
				f=0
	elif ch==2:
			print("operation on tupple")
			print("--"*50)
			t1=('c','c++','java','dbms','web','python')
			t2=(1,3,43,33)
			while True:
				print(t1,t2)
				print("\n1.slicing\n2.member\n3.iteration\n4.length\n5.concat\n6.max\n7.min\n8.count\n9.repet\n10exit")
				c=int(input("enter your choice"))
				if c==1:
					print(t1[0:2])
				elif c==2:
					print('c' in t1)
				elif c==3:
					for i in range(0,len(t1)):
						print(t1[i])
				elif c==4:
					print(len(t1))
				elif c==5:
					print(t1+t2)
				elif c==6:
					print(max(t2))
				elif c==7:
					print(min(t2))
				elif c==8:
					print(t1.count(c))
				elif c==9:
					print(t1*2)
				else:
					break
