def calculateFeet(distance):
    feet = distance * 5280
    
    return feet

def calculateInches(distance):
    inches = distance * 63360
    
    return inches

def calculateYards(distance):
    yards = distance * 1760
    
    return yards

def displayResult(distance, yards, feet, inches):
    print(str(distance) + " miles is equal to " + str(yards) + " yards and " + str(feet) + " feet and " + str(inches) + " inches.")

def getDistance():
    print("Enter distance in miles:")
    distance = float(input())
    
    return distance

# Main
# Reference: https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/function-examples/
# This program converts an input distance in miles to the same distance in yards, feet, and inches
distance = getDistance()
yards = calculateYards(distance)
feet = calculateFeet(distance)
inches = calculateInches(distance)
displayResult(distance, yards, feet, inches)
