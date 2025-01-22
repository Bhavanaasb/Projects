
# User_names = {"Sesharama":123,,
#                "Durga":456,,
#                "Bhairava":789,
#                "Rudraunsh":111,
#                "Shourya":100}
Name = "Rudraunsh"
Password = "123"
User_name = input("Entere your name")
Passwords = input("Entere your Password")
Atm = '''1.Credit
2.Debit
3.Mini Statement
4.Exit'''
Amount=1000
if Name==User_name and Passwords==Password:
    print(Atm)
    while True:
        Option=int(input("Enter the option:"))
        if Option==1:
            credit_amount=float(input("Enter the amount"))
            print("Amount after credited:",Amount+credit_amount)
        elif Option==2:
            debit_amount=float(input("Enter the amount"))
            print("Amount after debited:",Amount-debit_amount)
        elif Option==3:
            print("Mini Statement:",Amount)
        elif Option==4:
            break
else:
    print("incorrect")
