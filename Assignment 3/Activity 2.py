# This program converts an inputted age into approximate total lived months, days, hours, minutes, and secons
print("Enter age")
age = float(input())
months = age * 12
days = age * 365
hours = age * 365 * 24
minutes = age * 365 * 24 * 60
seconds = age * 365 * 24 * 60 * 60
print(str(age) + "age is" + str(months) + "months" + str(days) + "days" + str(hours) + "hours" + str(minutes) + "minutes" + str(seconds) + "seconds")
