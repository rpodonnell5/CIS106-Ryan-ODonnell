# This program converts an input distance in miles to yards, feet, and inches.

# References:
# https://www.testingdocs.com/flowchart-to-convert-distance ...

print("Please enter a distance in miles")
distance = float(input())

yards = distance * 1760
feet = distance * 5280
inches = distance * 5280 * 12

print(str(distance) + "miles is equal to " +
    str(yards) + "yards, or " +
    str(feet) + "feet, or " +
    str(inches) + "inches.")
