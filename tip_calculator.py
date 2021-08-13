#inputs and variables

bill = float(input("How much did your meal cost? "))

tip = int(input("how much tip do you want to add 15% , 18% 44or 20% ?? "))

tax = 0.05

#math calculations

tax_amt = bill * tax

tip_amt = bill * tip/100

total = bill + tip_amt + tax_amt

#printing

print(f"Your Bill is ${bill:.2f} and your tip is ${tip_amt:.2f} ")

print(f"Your total with tax is ${total:.2f}")