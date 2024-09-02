# Grade student based on marks

marks = int(input("enter a marks:"))
if(marks>=90):
    Grade = "A" #Indentation
elif(marks>=80 and marks<90):
    Grade = "B"
elif(marks>=70 and marks<80):
    Grade = "C"
elif(marks < 70):
    Grade = "D"
print("Grade of the student:", Grade)
