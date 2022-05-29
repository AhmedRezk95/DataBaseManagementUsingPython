
import os


def login():
    os.system('clear')
    logmail=input("Enter Login mail:\n")
    # Open
    DataBaseFile = open('DataBase.csv', 'r')
    for i in DataBaseFile.readlines():
        i = i.strip("\n")  
        user = i.split(",")
        if logmail == user[2]:
            os.system('clear')
            print("Mail found!")
            logpass=input("Enter Password:\n")
            while logpass != user[3]:
                print("password not matched, please try again")
                logpass=input("Enter Password again or press 0 to exit:\n")
                os.system('clear')
                if int(logpass) == 0:
                    DataBaseFile.close()
                    return False
            os.system('clear')
            print("Log in Success")
            DataBaseFile.close()
            return logmail
    print("Mail Not Found please sign up")
    DataBaseFile.close()
    # Move to registeration function
    return False


