'''
this program is to check the marks from three subjects and 
calculate the total and average and accordingly grade the 
syudent
'''
Sname=input("Enter the student name:")
S1mark=int(input("Enter the S1 mark:"))
S2mark=int(input("Enter the S2 mark:"))
S3mark=int(input("Enter the S3 mark:"))

Total=300

Total_Smark=S1mark+S2mark+S3mark
Avg_mark=Total_Smark/3

percentage=(Total_Smark/300)*100

print (Sname ,"has secured", Total_Smark ,"with an average of", Avg_mark , "and the percentage is" , percentage)

