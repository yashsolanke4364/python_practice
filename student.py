name = input("enter the student name: ")
a, b, c, d, e = [int(x) for x in input("enter the marks of five subjects: ").split()]
def total_marks():
    return a+b+c+d+e;
def percentage():
    return total_marks()/5;
result1=total_marks()
print(result1)
result2=percentage()
print(result2)
if percentage()>=90:
    print("A")
elif percentage()>=75:
    print("B")
elif percentage()>=60:
    print("C")
elif percentage()>=40:
    print("D")
else:
    print("F") 
       
