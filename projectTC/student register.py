def inputmark():
    print("enter student ID :")
    id= int(input())
    print("enter exam score:")
    exam=int(input())
    print("enter all test scores: ")
    mark1=int(input())
    mark2=int(input())
    mark3=int(input())
    mark4=int(input())
    mark5=int(input())
    mark6=int(input())
    mark7=int(input())
    sum=(mark1+mark2+mark3+mark4+mark5+mark6+mark7 )
    avge=sum/7
    print("test average is :" + str(avge))
    print("final mark is: ", compute_mark(avge,exams))
    print("letter grade is:" , getgrade (compute_mark(avge,exams)) )
    print_remark( getgrade (compute_mark(avge,exams)) )

    return avge 
def compute_mark(avge,exams):
    # final_mark = 0.4 'avge + 0.6 ' exam
    return final_mark
def getgrade (final_mark):
    if 90<= final_mark<=100:
        grade = "A"
    elif 80<= final_mark<=89:
        grade = "B"
    elif 70<= final_mark<=79:
        grade = "C"
    elif 60<= final_mark<=69:
        grade = "D"
    return grade

def print_remark(grade):
    if grade == "A":
        print("remark : excellent ")
    elif grade == "B":
        print("remark : good job")
    elif grade == "C":
        print("remark : Nice")
    elif grade == "D":
        print("remark : keep working")
    elif grade == "F":
        print("remark : Poor ")
inputmark()
# print("wow")
    







