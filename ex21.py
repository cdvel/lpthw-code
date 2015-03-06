def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	pass

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b
	pass

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	pass

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	pass

print "Let us do some math with just functions!"

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it anyway
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

where = ((9*2)*(5-3))-10;
where2 = substract(multiply(multiply(9,2),substract(5,3)),10)
print where == where2
