d={}
while True:
	print("\n select  one of the following")
	print("1:add an employee\n2:check the details of an employee\n3:exit\n")
	y=int(input("enter your choice\n"))
	if y==1:
		while True:
			name=input("enter the name of an employee\n")
			pan=(input("enter  pan number\n"))
			basic=int(input("enter the basic salary\n"))
			hra=(12/100)*basic
			da=(98/100)*basic
			pf=(16/100)*basic
			gross=hra+da-pf
			s1="{'pan no':"+str(pan)+","
			s2="'basic salary':"+str(basic)+"," 
			s3="'hra': "+str(hra)+",'da':"+str(da)+",'pf': "+str(pf)+",'gross salary':"+str(gross)+"}"
			r=s1+s2+s3
			d2=eval(r)
			d[name]=d2
			ad=int(input("do you want to add another employee(1/0):"))
			if ad==1:
				continue
			else:
				break
	elif y==2:
		res=not d
		if res==0:
			while True:
				print("\nlist of employee:")
				for i in d:
					print(i)
				n2=input("enter the name of the employee tocheck his details:")
				for i in d:
					if i==n2:
						#for j in d2:
							#print(j,":",d2[j])
						print(i,':',d[n2])

				x=int(input("do you want to continue(1/0):"))
				if(x==1):
					continue
				else:
					break
		else:
			print("dictionary is empty\n !!! add some employees!!!")
			break
	elif y==3:
		break
	else:
		print("enter a valid choice\n")
