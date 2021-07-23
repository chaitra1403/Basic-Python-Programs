class student:
    def __init__(self,usn='',name='',age=0):
        self.usn=usn
        self.name=name
        self.age=age

    def getdata(self):
        self.usn=input("Enter the usn:")
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))

class derived1(student):
    def __init__(self,sem=0,subj1=0,subj2=0,subj3=0,subj4=0,subj5=0):
        self.sem=sem
        self.subj1=subj1
        self.subj2=subj2
        self.subj3=subj3
        self.subj4=subj4
        self.subj5=subj5

    def getmarks(self):
        self.sem=input("Enter the  sem:")
        self.subj1=int(input("Enter subj1 marks:"))
        self.subj2=int(input("Enter subj2 marks:"))
        self.subj3=int(input("Enter subj3 marks:"))
        self.subj4=int(input("Enter subj4 marks:"))
        self.subj5=int(input("Enter subj5 marks:"))

class derived2(derived1):
    def total(self,tot_marks=0,avg=0):
        self.tot_marks=(self.subj1+self.subj2+self.subj3+self.subj4+self.subj5)
        self.avg=int((self.tot_marks/500)*100)

    def display(self):
        print("USN=",self.usn)
        print("Name=",self.name)
        print("AGe=",self.age)
        print("sem=",self.sem)
        print("subj1=",self.subj1)
        print("subj2=",self.subj2)
        print("subj3=",self.subj3)
        print("subj4=",self.subj4)
        print("subj5=",self.subj5)
        print("tot=",self.tot_marks)
        print("avg=",self.avg)
s=derived2()
s.getdata()
s.getmarks()
s.total()
s.display()
