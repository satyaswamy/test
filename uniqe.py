# This script is to check the list or array and get the uniqe data and print the number of occurance of the same 

Ilist=input("Enter the list of data with repeted items, seperated by ,:")
print(Ilist)

RepetedItems=dict((i, Ilist.count(i)) for i in Ilist)
print (RepetedItems)
