val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
val3 = int(input("Enter third number: "))
 
if (val1 > val2) and (val1 > val3):
   largest = val1
elif (val2 > val1) and (val2 > val3):
   largest = val2
else:
   largest = val3
 
print("The largest number is",largest)