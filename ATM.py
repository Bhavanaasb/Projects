username = 'krishna'
password = 'python123'

cust_name=input("Enter your user name:")
cust_password=str(input("Enter your password:"))

if cust_name==username and cust_password==password:
    print('''
    1.Deposite
    2.Withdraw
    3.Mini Statement
    4.Exit     
    ''')
    amount=50000
    option=int(input("Select your option:"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount+=dep
        print("Total Amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount:"))
        amount-=withd
        print("Total Amount:",amount)
    elif option==3:
        print("---------ATM---------")
        print("Username:",username)
        print("Total Amount:",amount)
        print("Thanks for visiting")
        print("---------------------")
    elif option==4:
        exit()
else:
    print("Please enter correct credentials")
    


