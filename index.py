#first time for me learn python lang
#I will win the ipad and lean more about progremming because that is my drean
#str()lett the int to sstring
print("Welcom to our Calcolater app")
num1=float(input("Enter number 1 :"))
oper=input("Choose an operation(+,-,*,/,%)")
num2=float(input("Enter number2 :"))
if oper=="+":
    result=num1+num2
    print(num1,"+" ,num2,"=" ,result)
elif oper=="-":
    result=num1-num2
    print(num1,"-", num2,"=",result)
elif oper=="*":
    result=num1*num2
    print(num1,"*",num2,"=",result)
elif oper=="/":
    result=num1/num2    
    print(num1,"/",num2,"=",result)
elif oper=="%":
    result=num1%num2
    print(num1,"%",num2,"=",result)
else :
    print("Add"+str(num1+num2),"Sub"+str(num1-num2),"Mult"+str(num1*num2),"Div"+str(num1/num2),"Mod"+str(num1%num2))
    
   