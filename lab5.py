class student:
    def __init__(self,usn='',name='',age=0):
        self.usn=usn
        self.name=name
        self.age=age

    def getdata(self):
        self.usn=input("Enter the usn:")
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))

    def display(self):
        print("USN=",self.usn)
        print("NAME=",self.name)
        print("AGE=",self.age)

class ugstudent(student):
    def __init__(self,sem=0,fees=0,stipend=0):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend

    def uginfo(self):
        self.sem=input("Enter the sem:")
        self.fees=int(input("Enter the fees:"))
        self.stipend=int(input("Enter the stipend:"))

    def ugdisplay(self):
        print("SEM=",self.sem)
        print("FEES=",self.fees)
        print("STIPEND=",self.stipend)

class pgstudent(student):
    def __init__(self,sem=0,fees=0,stipend=0):
        self.sem=sem
        self.fees=fees
        self.stipend=stipend

    def pginfo(self):
        self.sem=input("Enter the sem:")
        self.fees=int(input("Enter the fees:"))
        self.stipend=int(input("Enter the stipend:"))

    def pgdisplay(self):
        print("SEM=",self.sem)
        print("FEES=",self.fees)
        print("STIPEND=",self.stipend)


s1=ugstudent()
s2=pgstudent()
s1.getdata()
s1.uginfo()
s1.display()
s1.ugdisplay()
s2.getdata()
s2.pginfo()
s2.display()
s2.pgdisplay()
