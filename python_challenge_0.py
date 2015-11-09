# The python challenge
# Challenge #0
# By: Zach Brisson

# bits = 10
#Any exponent over 10 will use the 64 bit integer set. Old code. 
# Thought  the if statement could not parse integer. 

print "Hello, I do exponent math for you."

# print "If you could give me the exponent please"
# ^ Old code.

exponent = int(raw_input("If you could give me the exponent please: \n > "))
# prompt user for the base.

# print "Thank you. Now how many times are we multiplying %d on itself?" % (exponent)
# ^ old code

power = int(raw_input("Thank you. Now how many times are we multiplying %d on itself? \n > " % (exponent)))

if power > 10:
# Anything past the 10th power uses 64 bits? !Check the full reasoning behind this.!
	print "Wow! Python has to switch to 64 bits for that one."
else:
	pass
# fun little if else statement. 
solution = exponent ** power

print "I have done the math for you. When %d to the %d power, you get %d" % (exponent, power, solution)