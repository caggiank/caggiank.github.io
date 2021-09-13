# description: This program converts a decimal positive integer to both binary and hexidecimal
# author: Kevin Caggiano
# date: September,12,2021

print("This program converts a decimal positive integer to both binary and hexadcimal")
posInt=int(input("Enter a positive integer: "))
binV=bin(posInt)
hexV=hex(posInt)
print("The decimal value of "+str(posInt)+" is:")
print(str(binV)+" in binary")
print(str(hexV)+" in hexadecimal")
