def calculateDays(years):
    days = years * 365
    print(str(years) + " years is about equal to " + str(days) + " days")
    
    return days

def calculateHours(years):
    hours = years * 365 * 24
    print(str(years) + " years is about equal to " + str(hours) + " hours")
    
    return hours

def calculateSeconds(years):
    seconds = years * 365 * 24 * 60 * 60
    print(str(years) + " years is about equal to " + str(seconds) + " seconds")
    
    return seconds

def calculateMonths(years):
    months = years * 12
    print(str(years) + " years is about equal to " + str(months) + " months")
    
    return months

def getAge():
    print("Enter how old you are in years")
    years = float(input())
    
    return years

def getChoice():
    print("Type in either Months, Days, Hours, or Seconds for the the unit the user wants to know their age in.")
    choice = input()
    
    return choice

# Main
# This program asks for the user's age in years and the unit of either months, days, hours or seconds to convert their age into and displays the conversion.
# References: https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/condition-examples/
years = getAge()
choice = getChoice()
if choice == "Months" or choice == "months":
    months = calculateMonths(years)
else:
    if choice == "Days" or choice == "days":
        days = calculateDays(years)
    else:
        if choice == "Hours" or choice == "hours":
            hours = calculateHours(years)
        else:
            if choice == "Seconds" or choice == "seconds":
                seconds = calculateSeconds(years)
            else:
                print("INVALID INPUT")
