"""
Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales. The formulas for making the conversion are as follows: 
  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32
where Tc is the Celsius temperature and Tf is the Fahrenheit temperature.

The program should ask the user to input a temperature and then which conversion they would like to perform. 

Sample session
Temperature converter

Enter a temperature: 20
Convert to (F)ahrenheit or (C)elsius? F

20 C = 68 F

"""

temperature = input("Enter a temperature: ")
standard = input("Convert to (F)ahrenheit of (C)elsius? ")

def C_to_F(tC):
	tF = ((9 / 5) * int(tC)) + 32
	return tF

def F_to_C(tF):
	tC = (5 / 9) * (int(tF) - 32)
	return tC

if temperature.isnumeric() == False:
	print("That is not a number.")
else:
	if standard == "F":
		tF = C_to_F(temperature)
		print(str(temperature) + " " + "C" + " = " + str("%.2f" % round(tF,2)) + " " + standard)
	elif standard == "C":
		tC = F_to_C(temperature)
		print(str(temperature) + " " + "F" + " = " + str("%.2f" % round(tC,2)) + " " + standard)
	else:
		print("That is not F or C")

	