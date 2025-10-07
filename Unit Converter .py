print("Hellow too our Unit Converter web")
print("Choose what you want to convert:")
print("1-Weight")
print("2-height")
print("3-Temperature")
print("4-Time")
num=(input("please Enter your Converter "))
if num.lower() =="weight":
    print("Please select the unit")
    print("kg to g")
    print("g to kg")
    print("kg to lb")
    print("lb to kg")
    print("g to lb")
    print("lb to g")
    num2= input("Enter the unit : ")
    num1=float(input("Enter the number : "))
    if num2=="kg to g":
        result=num1*1000
        print("="+str(result)+"g")
    elif num2=="g to kg":
        result=num1/1000
        print("="+str(result)+"kg")
    elif num2=="kg to lb":
        result=num1*2.2
        print("="+str(result)+"lb")
    elif num2=="lb to kg":
        result=num1/2.2
        print("="+str(result)+"kg")
    elif num2=="g to lb":
        result=num1*0.00220462
        print("="+str(result)+"lb")
    elif num2=="lb to g":
        result=num1/0.00220462
        print("="+str(result)+"g")
    


    
    
    
        
    

    
    
    
    
    
