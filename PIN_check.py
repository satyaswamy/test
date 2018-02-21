'''
This script is to check the correct PIN no 
and after third attempt , it should close the window
informing the maximum tries
'''
count=0
PIN=123456
while (count<3):
	Puser=int(input("Enter the PIN:"))
	count+=1
	if (PIN==Puser):
		print("Sucess , PIN is matched at" , count, "time")
		break
	if (PIN!=Puser) and (count==3):

		print ("PIN is blocked, you have attempted the maximum time")
	else:

		print("Wrong PIN, try again")
