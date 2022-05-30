from datetime import datetime

# function to validate date in form of DD/MM/YYYY
def validate(d):
    try:
        return bool(datetime.strptime(d, '%d/%m/%Y'))
    except ValueError:
        return False


# Function to check and set end date > start date
def earlier(s,e):
    if validate(e):
        if datetime.strptime(s, "%d/%m/%Y").strftime('%d/%m/%Y') <= datetime.strptime(e, "%d/%m/%Y").strftime('%d/%m/%Y'):
            print("Valid start and end date")
            return True
        else:
            print("Not Valid,End date is ealier than Start date")
            return False
    else:
        print("Not a date, Please try again!")
        return False
        
