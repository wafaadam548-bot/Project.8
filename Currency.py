print("Welcome to Currency Converter<>")
print("_________________________________")
print ("USD")#done
print ("EUR")#done
print ("GBP")#done
print ("CAD")#done
print ("JPY")#done
print ("SAR")#done
print ("AED")#done
print ("QAR")#done
print ("BTC")#done
print ("ETH")#done
print ("USDT")#done
print ("CNY")#done
print ("INR")#done
print ("KRW")#done
print ("AUD")#done
print ("NZD")#done
print ("KWD")#done
print ("TRY")#done
print ("SYP")#done
coin=(input("Please Enter Your Currency :____"))
if coin=="USD":
    print("EUR")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="EUR":
        result= coin3*(0.93/1.0)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3*(1.00/0.9)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3*(3.67/1.0)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3*(0.79/1.0)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3*(150.12/1.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3*(7.32/1.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3*(34.50/1.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3*(1.37/1.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3*(1.53/1.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3*(84.10/1.00)
        print( "="+str(result) )
elif coin=="EUR":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3*(1.00/0.93)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3*(3.75/0.93)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3*(3.67/0.93)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3*(0.79/0.93)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3*(150.12/0.93)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3*(7.32/0.93)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3*(34.50/0.93)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3*(1.37/0.93)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3*(1.53/0.93)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3*(84.10/0.93)
        print( "="+str(result) )
elif coin=="SAR":
    print("USD")
    print("EUR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3*(1.00/3.75)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3*(0.93/3.75)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3*(3.67/3.75)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3*(0.79/3.75)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3*(150.12/3.75)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3*(7.32/3.75)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3*(34.50/3.75)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3*(1.53/3.75)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3*(1.53/3.75)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3*(84.10/3.75)
        print( "="+str(result) )
elif coin=="AED":
    print("USD")
    print("SAR")
    print("EUR")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3* (1.00 / 3.67)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 3.67)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3*(0.93/3.67)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3*(0.79/3.67)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3*(150.12/3.67)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3*(7.32/3.67)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3* (34.50 / 3.67)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 3.67)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 3.67)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 3.67)
        print( "="+str(result) )
elif coin=="GBP":
    print("USD")
    print("SAR")
    print("AED")
    print("EUR")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 0.79)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * ( 3.75/ 0.79)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 0.79)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 0.79)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 0.79)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 0.79)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 0.79)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 0.79)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 0.79)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 0.79)
        print( "="+str(result) )
elif coin=="JPY":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("EUR")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 150.12)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 150.12)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 150.12)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 150.12)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 150.12)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 150.12)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 150.12)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 150.12)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 150.12)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 150.12)
        print( "="+str(result) )
elif coin=="CNY":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("EUR")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 7.32)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 7.32)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 7.32)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 7.32)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 7.32)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 7.32)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 7.32)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 7.32)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 7.32)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 7.32)
        print( "="+str(result) )
elif coin=="TRY":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 34.50)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 34.50)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 34.50)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 34.50)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 34.50)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 34.50)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 34.50)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 34.50)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 34.50)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 34.50)
        print( "="+str(result) )
elif coin=="CAD":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("EUR")
    print("AUD")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 1.37)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 1.37)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 1.37)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 1.37)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 1.37)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 1.37)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 1.37)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 1.37)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 1.37)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 1.37)
        print( "="+str(result) )
elif coin=="AUD":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("EUR")
    print("INR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 1.53)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 1.53)
        print( "="+str(result) )
    elif coin2=="AED":
        result=coin3 * (3.67 / 1.53)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 1.53)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 1.53)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 1.53)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 1.53)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 1.53)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 1.53)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 1.53)
        print( "="+str(result) )
elif coin=="INR":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result= coin3 * (1.00 / 84.10)
        print( "="+str(result) )
    elif coin2=="SAR":
        result= coin3 * (3.75 / 84.10)
        print( "="+str(result) )
    elif coin2=="AED":
        result= coin3 * (3.67 / 84.10)
        print( "="+str(result) )
    elif coin2=="GBP":
        result= coin3 * (0.79 / 84.10)
        print( "="+str(result) )
    elif coin2=="JPY":
        result= coin3 * (150.12 / 84.10)
        print( "="+str(result) )
    elif coin2=="CNY":
        result= coin3 * (7.32 / 84.10)
        print( "="+str(result) )
    elif coin2=="TRY":
        result= coin3 * (34.50 / 84.10)
        print( "="+str(result) )
    elif coin2=="CAD":
        result= coin3 * (1.37 / 84.10)
        print( "="+str(result) )
    elif coin2=="AUD":
        result= coin3 * (1.53 / 84.10)
        print( "="+str(result) )
    elif coin2=="EUR":
        result= coin3 * (0.93 / 84.10)
        print( "="+str(result) )
elif coin=="QAR":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 3.64)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 3.64)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 3.64)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 3.64)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 3.64)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 3.64)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 3.64)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 3.64)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 3.64)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 3.64)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 3.64)
        print( "="+str(result) )
elif coin=="ETH":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 2600.00)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 2600.00)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 2600.00)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 2600.00)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79/ 2600.00)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 2600.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32/ 2600.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 2600.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 2600.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.37 / 2600.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 2600.00)
        print( "="+str(result) )        
elif coin=="BTC":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 60000.00)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 60000.00)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0,93 / 60000.00)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 60000.00)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 60000.00)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 60000.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 60000.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 60000.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 60000.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 60000.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 60000.00)
        print( "="+str(result) )      
elif coin=="USDT":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 1.00)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 1.00)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 1.00)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 1.00)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 1.00)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 1.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 1.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 1.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 1.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 1.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 1.00)
        print( "="+str(result) )
elif coin=="KRW":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 1400.00)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 1400.00)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 1400.00)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 1400.00)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 1400.00)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 1400.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 1400.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 1400.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 1400.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 1400.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 1400.00)
        print( "="+str(result) ) 
elif coin=="NZD":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 1.67)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 1.67)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 1.67)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 1.67)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 1.67)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 1.67)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 1.67)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 1.67)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 1.67)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 1.67)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 1.67)
        print( "="+str(result) )
elif coin=="KWD":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 3.25)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 3.25)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 3.25)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 3.25)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 3.25)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 3.25)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 3.25)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 3.25)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 3.25)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 3.25)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 3.25)
        print( "="+str(result) )                          
         
elif coin=="TRY":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 34.50)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 34.50)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 34.50)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 34.50)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 34.50)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 34.50)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 34.50)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 34.50)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 34.50)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 34.50)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 34.50)
        print( "="+str(result) )                          
         
elif coin=="SYP":
    print("USD")
    print("SAR")
    print("AED")
    print("GBP")
    print("JPY")
    print("CNY")
    print("TRY")
    print("CAD")
    print("AUD")
    print("INR")
    print("EUR")
    coin2=(input("Enter the currency you want to change to. :  "))
    coin3=float(input("Please Enter The amount "))
    if coin2=="USD":
        result=coin3 * (1.00 / 14500.00)
        print( "="+str(result) )
    elif coin2=="SAR":
        result=coin3 * (3.75 / 14500.00)
        print( "="+str(result) )
    elif coin2=="EUR":
        result=coin3 * (0.93 / 14500.00)
        print( "="+str(result) )    
    elif coin2=="AED":
        result=coin3 * (3.67 / 14500.00)
        print( "="+str(result) )
    elif coin2=="GBP":
        result=coin3 * (0.79 / 14500.00)
        print( "="+str(result) )
    elif coin2=="JPY":
        result=coin3 * (150.12 / 14500.00)
        print( "="+str(result) )
    elif coin2=="CNY":
        result=coin3 * (7.32 / 14500.00)
        print( "="+str(result) )
    elif coin2=="TRY":
        result=coin3 * (34.50 / 14500.00)
        print( "="+str(result) )
    elif coin2=="CAD":
        result=coin3 * (1.37 / 14500.00)
        print( "="+str(result) )
    elif coin2=="AUD":
        result=coin3 * (1.53 / 14500.00)
        print( "="+str(result) )
    elif coin2=="INR":
        result=coin3 * (84.10 / 14500.00)
        print( "="+str(result) )                                            
         
else :
    print ("Sorry make sure the spelling and every thing is right ---")   
    print("I am sorry if your contory not here I promess I will add later")       
          
          