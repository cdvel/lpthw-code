# -- coding: utf-8 --
name = 'César D.'
age = 33 # right now
height = 180 #cms
weight = 80 #kgs approx.
eyes = 'Brown'
teeth = 'White'
hair = 'Brownish'

print "Let's talk about %s."%name
print "He's %d cms tall(%d inches)." %(height, height*0.39)
print "He's %r kgs heavy(%d pounds)"%(weight, weight*2.2)

print "That's allright"
print "He's got %s eyes and %s hair"%(eyes,hair)
print "He's teeth are usually %s depending on the coffee"%teeth

#this line is tricky, get it right
print "If I add %d, %d, and %d, I get %d."%(age,height,weight, age+height+weight)

# https://docs.python.org/2/library/stdtypes.html#string-formatting

#'d' 	Signed integer decimal. 	 
#'i' 	Signed integer decimal. 	 
#'o' 	Signed octal value. 	(1)
#'u' 	Obsolete type – it is identical to 'd'. 	(7)
#'x' 	Signed hexadecimal (lowercase). 	(2)
#'X' 	Signed hexadecimal (uppercase). 	(2)
#'e' 	Floating point exponential format (lowercase). 	(3)
#'E' 	Floating point exponential format (uppercase). 	(3)
#'f' 	Floating point decimal format. 	(3)
#'F' 	Floating point decimal format. 	(3)
#'g' 	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. 	(4)
#'G' 	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. 	(4)
#'c' 	Single character (accepts integer or single character string). 	 
#'r' 	String (converts any Python object using repr()). 	(5)
#'s' 	String (converts any Python object using str()). 	(6)
#'%' 	No argument is converted, results in a '%' character in the result.