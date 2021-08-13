#input, variable

price = float(input("How much does your product cost? "))

tip = int(input("How much tip do you expect for this service? "))

tax = 15

#math

tax_amt = price * tax

tip_amt = price * tip/50

total = price + tip_amt + tax_amt

#print

print(f"Your Bill is ${price:.2f} and your tip is ${tip_amt:.2f} ")

print(f"Your total with tax is ${total:.2f}")

