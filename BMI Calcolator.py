print("Hello in our BMI web")
print("Lets calcoulate your BMI")
Tall=float(input("Please Enter Your Hight in Cm :"))
print("The hight is "+ Tall)
wight=float(input("Plese Enter your wight(kg) :"))
print("The wight is "+wight)
result=wight/Tall**2
print("your BMI is :"+ result)
if result<=18.5:
    print("UnderWight")
elif 18.5<= result<=24.5:
    print("Healthy")
elif 24.5<=result<= 29.9:
    print("OverWight")
elif 29.9<=result :
    print("Obesity")    
else:
    print("Sorry try again")