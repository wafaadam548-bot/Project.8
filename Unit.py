#append let us add option in the last
#insert let us add option in the bigging
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
elif num.lower()=="height":
    print("Please select the unit")
    print("km to m ")
    print("m to km")
    print("inch to cm")
    print("cm to inch")
    print("cm to mm")
    print("mm to cm")
    print("ft to m")
    print("m to ft")
    print("mm to cm")

    num2= input("Enter the unit : ")
    num1=float(input("Enter the number : "))
    if num2=="cm to m":
        result=num1/100
        print("="+str(result)+"m")
    elif num2=="m to cm":
        result=num1*100
        print("="+str(result)+"cm")
    elif num2=="km to m":
        result=num1*1000
        print("="+str(result)+"m")
    elif num2=="m to km":
        result=num1/1000
        print("="+str(result)+"km")
    elif num2=="inch to cm":
        result=num1*2.54   
        print("="+str(result)+"cm")
    elif num2=="cm to inch":
        result=num1/2.54
        print("="+str(result)+"inch")
    elif num2=="cm to mm":
        result=num1*10
        print("="+str(result)+"mm")
    elif num2=="mm to cm":
        result=num1/10
        print("="+str(result)+"cm")
    elif num2=="ft to m":
        result=num1*0.3048
        print("="+str(result)+"m")
    elif num2=="m to ft":
        result=num1/0.3048       
        print("="+str(result)+"ft")
elif num.lower()=="time":
    print("Please select the unit")
    print("Please select from the least and write it exact thing ")
    print("sec to min ")
    print("min to sec")
    print("min to hour")
    print("hour to min")
    print("sec to hour")
    print("hour to sec")
    print("min to day")
    print("day to min")
    print("sec to day")
    print("day to sec")
    print("hour to day")
    print("sec to year")
    print("year to sec")
    print("year to min")
    print("min to year")
    print("year to day")
    print("day to year")
    print("month to year")
    print("year to month")

    num2= input("Enter the unit : ")
    num1=float(input("Enter the number : "))
    if num2=="sec to min":
        result=num1/60
        print("="+str(result)+"min")
    elif num2=="min to sec":
        result=num1*60
        print("="+str(result)+"sec")
    elif num2=="min to hour":
        result=num1/60
        print("="+str(result)+"hours")
    elif num2=="hour to min":
        result=num1*60
        print("="+str(result)+"min")
    elif num2=="sec to hour":
        result=num1/3600   
        print("="+str(result)+"hour")
    elif num2=="hour to sec":
        result=num1*3600
        print("="+str(result)+"sec")
    elif num2=="min to day":
        result=num1/1440
        print("="+str(result)+"day")
    elif num2=="day to min":
        result=num1/1440
        print("="+str(result)+"min")
    elif num2=="sec to day":
        result=num1/86400
        print("="+str(result)+"days")
    elif num2=="day to sec":
        result=num1*86400       
        print("="+str(result)+"sec")
    elif num2=="hour to day":
        result=num1/24      
        print("="+str(result)+"days")
    elif num2=="day to hour":
        result=num1*24       
        print("="+str(result)+"hours")
    elif num2=="sec to year":
        result=num1/31536000       
        print("="+str(result)+"years")
    elif num2=="years to sec":
        result=num1*31536000       
        print("="+str(result)+"sec")
    elif num2=="min to year":
        result=num1/525600       
        print("="+str(result)+"years")
    elif num2=="year to min":
        result=num1*525600      
        print("="+str(result)+"min")
    elif num2=="hour to year":
        result=num1/8760      
        print("="+str(result)+"years")
    elif num2=="year to hour":
        result=num1*8760     
        print("="+str(result)+"hours")
    elif num2=="month to year":
        result=num1/12     
        print("="+str(result)+"years")
    elif num2=="year to month":
        result=num1*12   
        print("="+str(result)+"month")
elif num.lower()=="temperature":
    print("Please select the unit")
    print("c to f")
    print("f to c")
    print("c to k")
    print("k to c")
    print("f to k")
    print("k to f")
    num2= input("Enter the unit : ")
    num1=float(input("Enter the number : "))      
    if num2=="f to c":
        result=(num1 - 32) * 5/9
        print("="+str(result)+"c")
    elif num2=="c to f":
        result=(num1* 9/5) + 32
        print("="+str(result)+"f")
    elif num2=="c to k":
        result=num1+ 273.15
        print("="+str(result)+"k")
    elif num2=="k to c":
        result=num1 + 273.15
        print("="+str(result)+"c")
    elif num2=="f to k":
        result=(num1- 32) * 5/9 + 273.15   
        print("="+str(result)+"k")
    elif num2=="k to f":
        result=(num1- 273.15) * 9/5 + 32
        print("="+str(result)+"f")
        
else:
    print("Sorry, make sure you follow the steps and write with the same letters and spelling.")            
            
            








        


    
    
    
        
    

    
    
    
    
    
