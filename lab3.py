print("sets and dict")
while True:
	print("1.set\n2.dict\n")
	ch=int(input("enter your choice"))
	if ch==1:
		while True:
			print("--"*50)
			print("Sets\n\n0.disp\n1.union\n2.intersection\n3.symmetric diff\n4.differ\n5.add\n6.first element\n7.length\n8.member\n9.sizeof\n.10max\n11.min\n")
			print("--"*50)
			s1={1,2,3,8}
			s2={3,7,8,9}
			print(s1)
			print(s2)
			ch=int(input("enter ur ch"))
			if ch==1:
				print(s1.union(s2))
			elif ch==2:
				print(s1.intersection(s2))
			elif ch==3:
				print(s1.symmetric_difference(s2))
			elif ch==4:
				print(s1.difference(s2))
			elif ch==5:
				s1.add(10)
				print(s1)
			elif ch==6:
				print(s1.pop())
			elif ch==7:
				print(len(s1))
			elif ch==8:
				print(1 in s1)
			elif ch==9:
				print(s1.__sizeof__())
			elif ch==10:
				print(max(s1))
			elif ch==11:
				print(min(s1))
			elif ch==0:
				print(s1)
				print(s2)
			else:
				break
	elif ch==2:
		print("--"*50)
		print("dictinory")
		d1={'a':100,'b':200,'c':300}
		d2={'q':11,'ww':222,'s':111}
		while True:
			print("\n1.display\n2.insert\n3.copy\n4.display key\n5.display value\n6.add\n7.length\n8.membership\n\n10.clear")
			ch=int(input("enter you choice"))
			if ch==1:
				print(d1)
				print(d2)
			elif ch==2:
				d1["q"]=400
				print(d1)
			elif ch==3:
				d3=d1.copy()
				print(d3)
			elif ch==4:
				print(d1.keys())
			elif ch==5:
				print(d1.values())
			elif ch==6:
				print(d1.update(d2))
			elif ch==7:
				print(len(d1))
			elif ch==8:
				print('a' in d1)
			elif ch==9:
				d1.clear()
				print(d1)
			else:
				break
