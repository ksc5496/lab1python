temp1 = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit== "f":
  temp2 = (float(temp1)-32)*(5/9)
  print(str(temp1) + "° in Fahrenheit is equivalent to " + str(temp2) + "° in Celsius.")
elif unit == "C" or unit == "c":
  temp3 = ((float(temp1)*9/5)+32)
  print(str(temp1) + "° in Celsius is equivalent to " + str(temp3) + "° in Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")