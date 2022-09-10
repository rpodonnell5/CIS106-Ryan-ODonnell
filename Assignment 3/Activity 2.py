# This program converts an inputted age into approximate total lived months, days, hours, and seconds
# References:
# References go here ...
print("Please enter how old you are in years")
age = float(input())
months = age * 12
days = age * 365
hours = age * 365 * 24
seconds = age * 365 * 24 * 60 * 60
print("Your age is approximately equal to ...")
print("Months = " + str(months) + " months")
print("Days = " + str(days) + " days")
print("Hours = " + str(hours) + " hours")
print("Seconds = " + str(seconds) + " seconds")
