weight = input ("Input your weight: ")
unit = input ("for Kg type K and for pound type L: ")
if unit.upper() == "K":
    convert = float(weight)*2.20
    print ("your weight in lb is: " + str(convert))
else:
    convert = float (weight)/2.20
    print ("Your weight in Kg is: " + str(convert))
print ("Done")