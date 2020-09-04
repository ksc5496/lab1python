# Author: Krish Choudhary ksc5496@psu.edu
# Collaborator: Nicole Giron nqg5259@psu.edu
# Collaborator: Youhyun Kim yhk5109@psu.edu
# Collaborator: Geng Niu gjn5124@psu.edu

temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  temp = float(temp)
  temp1 = (temp-32)*(5/9)
  print(f'%s° in Fahrenheit is equivalent to %s° Celsius.'%(temp,temp1))
elif unit == "C" or unit == "c":
  temp = float(temp)
  temp2 = (9/5*temp)+32
  print(f'%s° in Celsius is equivalent to %s° Fahrenheit.'%(temp,temp2))
else:
  print(f'Invalid unit(%s).'%(unit))
