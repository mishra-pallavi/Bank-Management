import pathlib
import pickle
import os

class Account():

    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current : "))
        print("\n\n\nAccount Created")

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

def newAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)
    return

def depositAndWithdraw(account_no,type):
    file  = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        for item in mylist:
            if item.accNo == account_no:
                if type == 1:
                    amount = int(input("Enter amount to deposit : "))
                    item.deposit += amount
                    print("your account is updated")
                else:
                    amount = int(input("Enter amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    print("Insufficient amount")
    else:
        print("No recode to search")
    outfile = open("newaccount.data","wb")
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename("newaccount.data","accounts.data")



    return


def balanceEnquiry(account_no):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        found = False
        for item in mylist:
            if item.accNo == account_no:
                print(f"Your account balance is : {item.deposit}")
                found = True
    else:
        print("no record to search")
    if not found:
        print("no existing record with this account no")



def accountHolderList():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        mylist = pickle.load(infile)
        print("account no | account holder name | account type | amount")
        for item in mylist:
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else:
        print("No recode to display")
    return

def closeAccount(account_no):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != account_no:
                newlist.append(item)
        os.remove("accounts.data")
        outfile = open("newaccounts.data","wb")
        pickle.dump(newlist,outfile)
        outfile.close()
        os.rename("newaccounts.data","accounts.data")

def updateAccount(account_no):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        oldlist = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        for item in oldlist:
            if item.accNo == account_no:
                item.name = input("Enter the account holder name : ")
                item.type = input("Ente the type of account [C/S] : ")
                item.deposit = int(input("Enter The amount : "))
        outfile = open("newaccounts.data","wb")
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename("newaccounts.data","accounts.data")


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data","rb")
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open("newaccounts.data","wb")
    pickle.dump(oldlist,outfile)
    outfile.close()
    os.rename("newaccounts.data","accounts.data")


# start of the program
ch=''
num=0
intro()
 
while ch != 8:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input("Enter your choice : ")

    if ch == '1':
        newAccount()
    elif ch == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num,1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num,2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        balanceEnquiry(num)
    elif ch == '5':
        accountHolderList()
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        closeAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        updateAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else:
        print("Invalid choice")
    