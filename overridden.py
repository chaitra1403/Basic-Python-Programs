class a:
	amt=1.04
	def __init__(self,name=' ',id=' ',pay=' '):
		self.name=name
		self.id=id
		self.pay=pay
	def get(self): #id=' ',name=' ',pay=' '):
		self.id=int(input("enter the id"))
		self.name=input("enter the name")
		self.pay=int(input("enter the pay"))
	def payment(self): #,salary=' '):
		self.pay=int(self.pay*self.amt)
	def disp(self):
		print(self.id,self.name,self.pay)
class p(a):
	amt=2.04
	def payment(self):
		self.pay=int(self.pay*self.amt)
class q(a):
	amt=3.04
	def payment(self):
		self.pay=int(self.pay*self.amt)
b=p()
c=q()
b.get()
b.payment()
b.disp()
c.get()
c.payment()
c.disp()
