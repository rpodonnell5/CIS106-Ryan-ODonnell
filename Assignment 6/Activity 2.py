#This program asks the user for an age in years
#converts the given age in years to months, days, hours, and seconds
#and displays the results.
#
#References:
#https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/python-examples-3/

def get_years():
    print("Enter Age in years:")
    years = float(input())
    return years

def calculate_months(years):
    months = years*12
    return months

def calculate_days(years):
    days = years*365
    return days

def calculate_hours(years):
    hours = years*365*24
    return hours

def calculate_seconds(years):
    seconds = years*365*24*60*60
    return seconds

def display_result(years, months, days, hours, seconds):
    print(str(years) + " Years is approximately equal to " +
        str(months) + " Months, " +
        str(days) + " Days, " +
        str(hours) + " Hours, and " +
        str(seconds) + " seconds.")

def main():
    years = get_years()
    months = calculate_months(years)
    days = calculate_days(years)
    hours = calculate_hours(years)
    seconds = calculate_seconds(years)
    display_result(years, months, days, hours, seconds)
    
main()