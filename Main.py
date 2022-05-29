# Import all function from registeration python file
import os

from DropPro import DropProject
from EditPro import EditProject
from SearchPro import SearchProject
from ViewPro import ViewProjects
from AddProject import AddProjects
from loginFun import login
from registerFun import registeration


# Clear screen
os.system('clear')

while True:
    selection=input("----------------------------------------------------------------------\nselect your choice: \n1)Login\n2)Register\n3)exit\n----------------------------------------------------------------------\n-> ")
    if selection.isdigit():
        if int(selection) == 1:
            # 1- mail login
            mail=login()
            # in case mail log in failed
            if mail == False:
                continue
            while True:
                selection=input("----------------------------------------------------------------------\nselect your choice: \n1)Add\n2)view\n3)edit\n4)delete\n5)search based on date\n6)exit\n----------------------------------------------------------------------\n->")
                if selection.isdigit():
                    if int(selection) == 1:
                        AddProjects(mail)
                    # if he press 2 -> view all projects
                    elif int(selection) == 2:
                        ViewProjects()
                    # if he press 3 -> edit own projects
                    elif int(selection) == 3:
                        EditProject(mail)
                    # if press 4 -> delete row
                    elif int(selection) == 4:
                        DropProject(mail)
                    # Search for project using dates
                    elif int(selection) == 5:
                        SearchProject()
                    # Exit Button
                    elif int(selection) == 6:
                        os.system('clear')
                        break
                    else:
                        os.system('clear')
                        print("Not Valid Number, Try Again")
                else:
                    os.system('clear')
                    print("Empty/String error, Enter Again")
        if int(selection) == 2:
            os.system('clear')
            reg = registeration()
            if reg == False:
                continue
        if int(selection) == 3:
            os.system('clear')
            break
        else:
            os.system('clear')
            print("Not Valid Number, Try Again")
    else:
        os.system('clear')
        print("Empty/String error, Enter Again")
    