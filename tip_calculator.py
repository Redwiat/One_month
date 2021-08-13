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


# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)
# Get a name
name = input("What is you're name? ")
print(name)

total = int(float(input("What is you're bill sub-total? ").replace('$', '')))
print(total)

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print(f"15% is ${tip_15:.2f}")
print(f"18% is ${tip_18:.2f}")
print(f"20% is ${tip_20:.2f}")


# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)

total = float(input("What is you're bill sub-total? ").strip('$'))

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print("Tip Suggestions:")
print("----------------")
print(f"15% is ${tip_15:.2f}")
print(f"18% is ${tip_18:.2f}")
print(f"20% is ${tip_20:.2f}")
