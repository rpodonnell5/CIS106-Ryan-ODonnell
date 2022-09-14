# This program converts an input distance in miles to yards, feet, and inches.

print("Please enter a distance in miles")
distance = float(input())

yards = distance * 1760
feet = distance * 5280
inches = distance * 63360

print(str(distance) + "miles is equal to " + str(yards) + "yards, or " + str(feet) + "feet, or " + str(inches) + "inches.")

# Reference: https://www.testingdocs.com/flowchart-to-convert-distance-in-kilometers-to-miles/
