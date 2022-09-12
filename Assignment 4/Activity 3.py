# This program converts an input distance in miles to yards, feet, and inches.

# Reference: 
#   https://www.testingdocs.com/flowchart-to-convert-distance ...

print("Please enter a distance in miles")
distance = float (input())
yards = distance * 1760
feet = distance * 5280
inches = distance * 63360
print("The distance given is equal to...")
print ("Yards = " + str(yards) + " yards")
print ("Feet = " + str(feet) + " feet") 
print ("Inches = " + str(inches) + " inches")

