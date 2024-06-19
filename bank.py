import datetime
def bank():
    name=input("Name:")
    password=input("Password:")
    emailid=input("Emailid:")
    transaction_pin=int(input("Transaction PIN:"))
    contact=int(input("Contact#"))
    date=datetime.datetime.now()
    print("Name:",name)
    print("Password",password)
    print("Emailid",emailid)
    print("Transaction PIN",transaction_pin)
    print("Contact#",contact)
    print("datetime",date)

