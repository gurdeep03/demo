

z="Yes"
while z=="Yes":
    print(" Other Currency Converter in Indian Currency ")
    x=int(input("Enter the Ammount \n"))
    y=input("Enter Currency name \n")
    y=(y.capitalize())
    if y=="Us Dollar":
        print(x,"Us Dollar is equal to",x*81.13,"Indian rupees")
    
    elif y== "Indian rupee":
        print(x,"Indian rupee is equal to",x*1,"Indian rupees")   
    
    elif y=="Euro":
        print(x,"Euro is equal to",x*88.18,"Indian rupees")
    
    elif y=="Fram":
        print(x,"Fram is equal to",x*0.21,"Indian rupees")
    
    elif y=="Florin":
        print(x,"Florin is equal to",x*45.37,"Indian rupees")
    
    elif y=="Dinar":
        print(x,"Dinar is equal to",x*266.03,"Indian rupees")
    
    elif y=="Taka":
        print(x,"Taka is equal to",x*0.81,"Indian rupees")
    
    elif y=="Ruble":
        print(x,"Rulble is equal to",x*1.35,"Indian rupees")
    
    elif y=="Ngultrum":
        print(x,"Ngultrum is equal to",x*1,"indian rupees")
    
    elif y=="Pula":
        print(x,"Pula is equal to",x*6.33,"Indian rupees")
    
    elif y=="Yuan":
        print(x,"Yuan is equal to",x*11.38,"Indian rupees")
    
    elif y=="Peso":
        print(x,"Peso is equal to",x*1.44,"Indian rupees")
    
    elif y=="Lev":
        print(x,"Lev is equal to",x*43.46,"Indian rupees")
    
    elif y=="Yen":
        print(x,"Yen is equal to",x*0.58,"Indian rupees") 
    
    elif y=="Manat":
        print(x,"Manat is equal to",x*46.99,"Indian rupees")       
    
    elif y=="Shekel":
        print(x,"Shekel is equal to",x*23.24,"Indian rupees") 
    
    elif y=="Canadian Dollar":
        print(x,"Canadian Dollar is equal to",x*60.73,"Indian rupees")  
    
    elif y=="Australian Dollar":
        print(x,"Australian is equal to",x*55.53,"Indian rupees")  
    
    elif y=="New Zealand Dollar":
        print(x,"New Zealand Dollar is equal to",x*52.57,"Indian rupees")           
    
    else:
        print("please enter the currency name properly")
    
    z=input("Enter ""yes"" for continue, ""No"" for exit \n")
    
    z=(z.capitalize())
    
    


