def calculateDays(years):
    days = years * 365
    
    return days

def calculateMonths(years):
    months = years * 12
    
    return months

def calculateHours(years):
    hours = years * 365 * 24
    
    return hours

def calculateSeconds(years):
    seconds = years * 365 * 24 * 60 * 60
    
    return seconds

def displayResult(years, result, label):
    print(str(years) + " years is about equal to " + str(result) + " " + label + ".")

def getAge():
    print("Enter how old you are in years")
    years = float(input())
    
    return years

def getChoice():
    print("Type in either M for Months, D for Days, H for Hours, or S for Seconds for the the unit the user wants to know their age in.")
    choice = input()
    
    return choice

def processDays(years):
    result = calculateMonths(years)
    displayResult(years, " years is about equal to ", result, " Months.")

# Main
# This program asks for the user's age in years and the unit of either months, days, hours or seconds to convert their age into and displays the conversion.
# References: https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/condition-examples/
years = getAge()
choice = getChoice()
if choice == "M" or choice == "m":
    months = calculateMonths(years)
    displayResult(years, months, "months")
else:
    if choice == "D" or choice == "d":
        days = calculateDays(years)
        displayResult(years, days, "days")
    else:
        if choice == "H" or choice == "h":
            hours = calculateHours(years)
            displayResult(years, hours, "hours")
        else:
            if choice == "S" or choice == "s":
                seconds = calculateSeconds(years)
                displayResult(years, seconds, "seconds")
            else:
                print("INVALID INPUT")
