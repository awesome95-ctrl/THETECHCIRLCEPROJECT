print("select an operation")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input()

if operation == "1":
   num1 = input( " enter first number " )
   num2 = input ( " enter second number " )
   print("the sum is "+ str(int(num1) + int(num2)))
elif operation == "2":
     num1 = input( " enter first number " )
     num2 = input ( " enter second number " )
     print("The subtraction of num1 and num 2 "+  str(int(num1) - int(num2)))
elif operation == "3":
   num1 = input (" enter first number ")
   num2 = input  (" enter second number ")
   print("The multiplication of num1 and num2 is "+ str(int( num1 ) * int( num2 )))
elif operation == "4":
     num1 = input ( " enter first number " )
     num2 = input ( " enter second number ")
     print("The division of num1 and num2 is "+ str(int( num1 ) / int( num2 )))
else:
    print("please input a number")

