# Strings are text surrounded by quotes
# Both single (') or double (") or triple (""") quotes are used
# examples: "USA", '211', "I'm lovin' it!"


# Strings are text surrounded by quotes  (single, double, or triple) quotes. 

# Here's another example using a variable: 

kanye_quote = "my greatest pain in live is that I will never be able to see myself perform live"

print("kanye_quote") 

# The command line will print out the string without the quotes. 
# The Kanye quote is long, but if you want to break it up into multiple lines you can use triples-quotes """:

kanye_quote = """My greatest pain in life
is that I will never be able
to see myself perform live."""


# Escaping quotes in strings

# So if you want to use single or double-quotes in a string without closing it out, 
# you have to "escape" it by putting a backslash (\) in front of it:

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\""

print(hamilton_quote)

# It never hurts to put a \ in front of a quotation mark. 
# You can also add newlines or tabs to strings with \n and \t.
# There are other characters you will need to escape. For example, 
# in order to use a backslash in a string
# you actually have to escape the backslash like this: \\.
# Triple quotes are another way to use either single or double quotations within a string. 
# Like so: 

# It never hurts to put a \ in front of a quotation mark. 
# You can also add newlines or tabs to strings with \n and \t.
# There are other characters you will need to escape. For example, 
# in order to use a backslash in a string, 
# you actually have to escape the backslash like this: \\.
# Triple quotes are another way to use either single or double quotations within a string. 
# Like so: 

"""Well, the word got around, they said, "This kid's insane, man"""

# variables are name
# there plain, lowercase words
# examples: x, y, apple, phone_a_quail

name = "Redwan"
banana_fee = 500
apple_fee = 120

total = banana_fee + apple_fee

print(name, "the total will be", total)

# print(name, "the total will be", total)
print(f"{name} the total will be {total}")

# print(name, "the total will be", total)
print(f"{name} the total will be ${total:.2f}")

