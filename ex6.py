x = "Thre are %d types of people." %10
binary = "binary"
do_not = "don't"
# prepare in variable output of both variables
y = "Those who know %s and those who %s."%(binary,do_not)

print x
print y

print "I said: %r." % x		#print anything!
print "I also said: '%s'." % y	

#allow joke variable to have a parameter!!! useful
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

# concatenate string
print w + e