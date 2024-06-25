'''
Day 2 Understanding DataTypes
Topics: Data Types, Numbers, Operations, Type Converstion, f-strings
Project: Tip Calculator

Type converstions: dataType(variable)
If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
'''
people = int(input("How many people are in your party?: "))
bill = float(input("How large was your bill?: "))
tip = float(input("How much do you want to tip? "))

tip_percentage = tip/100
# find the tip value of the bill based off the percentage
bill_tip = bill * tip_percentage

# calculate the total cost of the bill with the tip do determine the cost per person
total_bill = bill + bill_tip
bill_per_person = total_bill / people

# round the final amount per requirement of formatting the result to 2 decimal places
final_amt = round(bill_per_person, 2)
print(f"Each person should pay {final_amt} dollar(s)")
