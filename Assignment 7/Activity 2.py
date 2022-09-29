def calculateDays(age):
    days = age * 365
    
    return days

def calculateHours(age):
    hours = age * 365 * 24
    
    return days

def calculateMonths(age):
    months = age * 12
    
    return months

def calculateSeconds(age):
    seconds = age * 365 * 24 * 60
    
    return seconds

def displayResult(age, fromScale, result, toScale):
    print(str(age) + fromScale + str(result) + toScale)

def getAge(scale):
    print("Enter age in years.")
    age = float(input())
    
    return age

def getChoice():
    print("Type in either months, days, hours, or seconds to convert a given age in years")
    choice = input()
    
    return choice

def processDays():
    age = getAge("Days")
    result = calculateDays(age)
    displayResult(age, " years is equal to ", result, " Days.")

def processHours():
    age = getAge("Hours")
    result = calculateHours(age)
    displayResult(age, " years is equal to ", result, " Hours.")

def processMonths():
    age = getAge("Months")
    result = calculateMonths(age)
    displayResult(age, " years is equal to ", result, " Months.")

def processSeconds():
    age = getAge("Seconds")
    result = calculateSeconds(age)
    displayResult(age, " years is equal to ", result, " Seconds.")

# Main
choice = getChoice()
if choice == "Months" or choice == "months":
    processMonths()
else:
    if choice == "Days" or choice == "days":
        processDays()
    else:
        if choice == "Hours" or choice == "hours":
            processHours()
        else:
            if choice == "Seconds" or choice == "seconds":
                processSeconds()
            else:
                print("You must enter Months, Days, Hours, or Seconds to convert your age.")
