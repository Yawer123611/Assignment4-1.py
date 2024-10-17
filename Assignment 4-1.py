charge = 0.00
charge = 35.008
numbChars = int(input("Please enter the number of characters you wish for: "))
woodType = input("Enter a wood type: ")
color = input("Enter a color: ")


#if statements

if numbChars > 5:
    charge = charge + (numbChars - 5) * 4.00


if woodType == "oak":
    charge = charge + 20.00

if color == "gold":
    charge = charge + 15.00

#print statements
print(f"The charge for this sign is: ${charge:.1f}")
