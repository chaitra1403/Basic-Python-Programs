class over:
	def __init__(self):
		self.alist=[]
	def getdata(self):
		n=int(input("enter the limit"))
		for i in range (0,n):
			item=int(input("enter the item"))
			self.alist.append(item)
		return self.alist
	def __add__(self,other):
		newlist=[]
		for i in range(0,len(self.alist)):
			newlist.append(self.alist[i]+other.alist[i])
		return newlist
	def __sub__(self,other):
		newlist=[]
		for i in range(0,len(self.alist)):
			newlist.append(self.alist[i]-other.alist[i])
		return newlist
	def __mul__(self,other):
		newlist=[]
		for i in range(0,len(self.alist)):
			newlist.append(self.alist[i]*other.alist[i])
		return newlist
	def __truediv__(self,other):
		newlist=[]
		for i in range(0,len(self.alist)):
			newlist.append(self.alist[i]/other.alist[i])
		return newlist
	def __floordiv__(self,other):
		newlist=[]
		for i in range(0,len(self.alist)):
			newlist.append(self.alist[i]//other.alist[i])
		return newlist
