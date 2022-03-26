# Sample Project: Modeling Shear and Moment on a Simply Supported Beam Using Python
# while True loop asks for the user to input units, and checks whether the units align with (SI units vs.
# USCS units)
while True:
    lengthUnit = input("Input unit for length of beam: either mm, cm, m, in, or ft ")
    # Checks whether SI or USCS units are used
    if lengthUnit == "ft" or lengthUnit == "in":
        loadUnit = input("Input unit for applied load: either lb or kip ")
        if loadUnit == "lb" or loadUnit == "kip":
        # Checks for the corresponding USCS force unit
            break
        else:
            print("Units do not match. Please try again.")
    elif lengthUnit == "mm" or lengthUnit == "cm" or lengthUnit == "m":
        loadUnit = input("Input unit for applied load: either N or kN ")
        if loadUnit == "N" or loadUnit == "kN":
            break
        else:
            print("Units do not match. Please try again.")
            # If the units do not align, an error is given and the user is asked to input the values
            # again.
            print(' ')

# Defines the moment unit by multiplying the distance and force units.
momentUnit = loadUnit + "-" + lengthUnit
print(" ")

# This prints out the unit to be used.
print("Length will be given in " + lengthUnit)
print("Loads will be given in " + loadUnit)
print("Moments will be given in " + momentUnit)
print(" ")

# For a concentrated load located at the center of the beam
beamLength = int(input('Input length of beam in ' + lengthUnit + ': '))
clcMagnitude = int(input('Input magnitude of concentrated load at center of beam in ' + loadUnit +
', where positive represents an upwards load: '))
print(" ")

clcEndLoad = str(clcMagnitude * 0.5)
clcMaxMoment = str(clcMagnitude * beamLength * 0.25)

# For a uniformly distributed load across the entire length of the beam
udlMagnitude = int(input('Input magnitude of uniformly distributed across the entire length of the'
+ ' beam in ' + loadUnit + ', where positive represents an upwards load: '))
print(" ")

udlEndLoad = str(udlMagnitude * clcMagnitude * 0.5)
udlMaxMoment = str(clcMagnitude * beamLength**2 * (1/8))

totalEndLoad = str(clcEndLoad + udlEndLoad)
totalMaxMoment = str(clcMaxMoment + udlMaxMoment)

totalMaxMomentLoc = str(beamLength * 0.5)
print('The magnitude of the loads at the ends of the beam are ' + clcEndLoad + ' '
+ loadUnit + ".")
print("The magnitude of the maximum moment is " + clcMaxMoment + " " + momentUnit + " and is located at "
+ totalMaxMomentLoc + " " + lengthUnit + ".")
