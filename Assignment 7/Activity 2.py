def getAge():
    print("Enter an age in years")
    years = float(input())
    
    return years

def getChoice():
    print("Type in either Months, Days, Hours, or Seconds for the choice of conversion from years.")
    choice = input()
    
    return choice

# Main
years = getAge()
choice = getChoice()
if choice == "Months" or choice == "months":
    months = years * 12
    print(str(years) + " years is about equal to " + str(months) + " months")
else:
    if choice == "Days" or choice == "days":
        days = years * 365
        print(str(years) + " years is about equal to " + str(days) + " days")
    else:
        if choice == "Hours" or choice == "hours":
            hours = years * 365 * 24
            print(str(years) + " years is about equal to " + str(hours) + " hours")
        else:
            if choice == "Seconds" or choice == "seconds":
                seconds = years * 365 * 24 * 60 * 60
                print(str(years) + " years is about equal to " + str(seconds) + " seconds")
            else:
                print("INVALID INPUT")
