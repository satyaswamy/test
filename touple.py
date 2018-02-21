'''
This is to print data from a touple 
'''
i=0
T=[]
while (i<5):
	Tdata=input("Enter touple data:")
	T.append(Tdata)
	i+=1
print ("The entered data in the touple is:----->",T)

print("<-----------------The touple in numbered list:---------------->")
count=1
for i in T:
	print(count,".",i)
	count=+1
