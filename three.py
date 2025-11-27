
#ATM application using python functions

def Trans():
    pin=1234
    bal=5000
    rpin = int(input("Enter your Pin :"))
    if rpin == pin :

        print("Authentication Success.")
        
        amt=int(input("Enter Amount to withdraw : "))
        
        if amt <= bal :
            print("Transaction Success.")
            print("Collect your cash.")
            print("Drawn Amount : ",amt)
            bal=bal-amt
            print("Remaining Balance : ",bal)
        else:
            print("Transaction Failed ,insuff balance....")
    else:
        print("Authentication Failed.")



    
Trans()  
