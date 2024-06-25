# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
format_weight = int(weight)

# height formatted to a float data type to allow for decimals
format_height = float(height)
# use the exponent **
bmi = int(format_weight / format_height ** 2)
print(bmi)
