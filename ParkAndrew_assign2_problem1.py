"""
Assignment #2, Part 1
Andrew Park
"""


#ask for user input, 2 3 digit numbers
digit1 = int(input("Enter a 3 digit number between 000 and 999: "))
digit2 = int(input("Enter a 3 digit number between 000 and 999: "))

print()

#find the digit in the ones place. Use % 10 to find the remainder which will be the ones digit
ones1 = digit1 % 10
ones2 = digit2 % 10
print("Digits in the 1's places: ", format(str(ones1), ">3s"), "and", ones2)

#find the digit in the tenths place. Use // 10 to turn it into an integer getting rid of the ones place. then find the remainder
#after dividing it by 10 again withi modulo.
tenths1 = (digit1 // 10) % 10
tenths2 = (digit2 // 10) % 10
print("Digits in the 10's places: ", format(str(tenths1), ">2s"), "and", tenths2)

#find the digit in the hundreds place
#divide the 3 digit number by 100 with // to get rid of the remainder and only isolating the 100's place.
hundreths1 = (digit1 // 100)
hundreths2 = (digit2 // 100)
print("Digits in the 100's places: ", hundreths1, "and", hundreths2)

print()

print("Graphical representation of your numbers")

print()

print((format("Hundreds", "<15s")), (format("Tens", "<15s")), (format("Ones", "<20s")))
#then print the digits a certain number of times
print((format(str(hundreths1)*hundreths1, "<15s")), format(str(tenths1)*tenths1, "<15s"), format(str(ones1)*ones1, "<20s"))
print((format(str(hundreths2)*hundreths2, "<15s")), format(str(tenths2)*tenths2, "<15s"), format(str(ones2)*ones2, "<20s"))

print()

#computing the super number
print("Computing Your Super Number!")

print()

#add each place value for both nunmbers combined
print("Step #1: Add Each Place Value")
hundreths3 = (hundreths1 + hundreths2)
print("- Hundreds:", hundreths1, "+", hundreths2, "=", hundreths3)

tenths3 = (tenths1 + tenths2)
print("- Tens:", format(str(tenths1), ">5s"), "+", tenths2, "=", tenths3)

ones3 = ones1 + ones2
print("- Ones:", format(str(ones1), ">5s"), "+", ones2, "=", ones3)

print()

#combine the values to be a string
print("Step #2: Combine New Values")
#turn to string to concatnate together.
combine1 = (str(hundreths3) + str(tenths3) + str(ones3))
print("-", hundreths3, "+", tenths3, "+", ones3, "=", combine1)

print()

#Compute the sum of digits in first number
print("Step #3: Compute The Sum of All Digits in First Number")
#combine the first number together
combinefirst = (hundreths1 + tenths1 + ones1)
print("-", hundreths1, "+", tenths1, "+", ones1, "=", combinefirst)

print()

#same thing but for second number
print("Step #4: Compute The Sum of All Digits in Second Number")
combinesecond = (hundreths2 + tenths2 + ones2)
print("-", hundreths2, "+", tenths2, "+", ones2, "=", combinesecond)

print()

#combining step3, step2, and step4 CONCATENATE, NOT ADD
print("Step #5: Combine The Numbers In This Order -- Step 3 + Step 2 + Step 4")
total = (str(combinefirst) + str(combine1) + str(combinesecond))
print("-", total)

