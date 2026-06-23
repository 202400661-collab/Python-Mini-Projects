name=input("Enter student name:")
attendance=float(input("Enter attendance percentage:"))
internal_mark=float(input("Enter internal mark of 25:"))
external_mark=float(input("Enter external mark of 75:"))
#total
total=internal_mark+external_mark
#percentage
percentage=(total/100)*100
#grade
if percentage>=90 and attendance>=90:
    grade="A+"
    performance="Excellent"
elif percentage>=80:
    grade="A"
    performance="very good"
elif percentage>=70:
    grade="B"
    performance="good"
elif percentage>=60:
    grade="C"
    performance="Average"
elif percentage>=50:
    grade="D"
    performance="Needs improvement"
else:
    grade="F"
    performance="Fail"
#OUTPUT
print("\n----STUDENTS PERFORMANCE REPORT---")
print("student name:",name)
print("Attendance:",attendance,"%")
print("Internal mark:",internal_mark)
print("External mark:",external_mark)
print("Percentage:",percentage,"%")
print("Grade:",grade)
print("Performance:",performance)
