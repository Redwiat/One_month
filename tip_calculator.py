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



#Sam's code

# This script takes an input from the user for a restaurant check in USD.
# After a 1- to 2-sentence description of each tipping rate, 
# it provides a guide on how much a tip of 15%, 18%, and 20% would total.
# It then prompts the user for the rate of tip they wish to leave. 
# Finally, it provides the bill amount, tip amount, and grand total.

import os
os.system('clear')                       # start with a blank screen

########### G A T H E R  B A S I C  I N F O #####################                   

name = input("What is your name? ")
restaurant = input("What is the name of the restaurant? ")
check = float((input("What is the total amount of the check, in U.S. Dollars (example: 18.29)? $")))

########## C A L C U L A T I O N S   F O R   P A R T  I ##############

tip_amt_15 = float( check * 15  / 100 )   # calc 15% tip rate: display in Part I
tip_amt_18 = float( check * 18  / 100 )   # calc 18% tip rate: display in Part I
tip_amt_20 = float( check * 20  / 100 )   # calc 20% tip rate: display in Part I
gt15 = float( check + tip_amt_15 )        # calc Grand Total: display in Part I - 15%
gt18 = float( check + tip_amt_18 )        # calc Grand Total: display in Part I - 18%
gt20 = float( check + tip_amt_20 )        # calc Grand Total: display in Part I - 20%

#################### D I S P L A Y  P A R T  I ##############################

print()
print("===============================================================================")
print(f" Okay, {name}, you say your check at {restaurant} was ${check:.2f}")
print("  so you should decide at which rate you wish to tip.")
print("     Read the following brief guidelines then select your tip rate.")
print(" NOTE: you don't have to pick one of these...you can make your rate anything. ")
print()
print("  15% - Server was slow to arrive, slow with drinks, generally unpleasant")
print()
print("  18% - Server was average in arriving at the table, was average in")
print("        getting out the drinks, forgot something on the order")
print()
print("  20% - Server was quick in all aspects, knew the menu well, refilled")
print( "        drinks without being asked, suggested particular dishes, and")
print("        offered dessert")
print()
print("  Tip & Grand Totals for suggested levels provided for your convenience:")
print()
print("       15%         18%          20%")
print(f"      ${tip_amt_15:.2f}       ${tip_amt_18:.2f}        ${tip_amt_20:.2f}    ")
print(f"      ${gt15:.2f}      ${gt18:.2f}       ${gt20:.2f}    ")
print() 
print("===============================================================================")
print()

rate = float(input("Enter your desired tip rate (example: 15): "))

tip = float(check * rate / 100)
grand_total = float(check + tip)

#################### D I S P L A Y  P A R T  II ##############################

print()
print(f"""{name}, your check amount for {restaurant} was ${check:.2f} 
and you generously selected {rate:.2f} percent as your tip rate.
Your tip amount is ${tip:.2f} 
which makes your Grand Total ${grand_total:.2f}""")
print()
print()


@sarah's code
import random

#Input from server
server_name = input("Hello Kick Ass Steak House servant, please enter your name.\n")
sub_total = float(input(f"Thank you {server_name}, please enter the subtotal of the patron's meal without the dollar sign ($)\n"))
rounded_subtotal = float(f"{sub_total:.2f} \n")

server_passover = input(f"Great {server_name}.  Now hit [ENTER] and pass the device to the patron\n")

#Input from patron
patron_name = input("We hope you enjoyed your meal at Kick Asss Steak House, can I please get your name?\n")

tip_selection = int(input(f"Thank you {patron_name}. The subtotal for your meal is ${rounded_subtotal}.\n" 
	"Please enter your tip percentage (15, 18, 20): \n" 
	"15 - average service\n"
	"18 - good service\n"
	"20 - fantastic service\n"))

#Convert inputs to manipulate mathematically
converted_subtotal = float(rounded_subtotal)	 
total = (converted_subtotal * ( 1 + tip_selection /100))

salutation = ["Thank you for visiting us",
	"We hope to see you again soon",
	"Have a safe drive home"]

random_salutation = random.choice(salutation)

#Final messsage for patron showing total with tip
print(f"{random_salutation} {patron_name}.\n")
print(f"Your total with tip is ${total:.2f} \n")

thoughts = ["Man, what a cheapskate.  Hope they don't come back!",
	"Interesting tip, looks like they're celebrating big tonight!",
	"That person just gave me their number.  Going to give them a call after my shift for some - Netflix and Chill!"]

#Bonus thoughts from waiters and waitress at Kick Ass Steak House
random_thoughts = random.choice(thoughts)

see_thoughts = input("BONUS: Hit [ENTER] to see what our waiters & waitresses really thought of their patrons\n")
print(random_thoughts)


#john's code
# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)
# Get a name
name = intut("What is your name? ")
print(name)

total = int(float(input("What is your bill sub-total? ").replace('$', '')))
print(total)

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print(f"15% is ${tip_15:.2f}")
print(f"18% is ${tip_18:.2f}")
print(f"20% is ${tip_20:.2f}")
