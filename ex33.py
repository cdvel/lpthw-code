def loop_function(numbers, top, step):
	i = 0

	#for i in range(0, top, step):
	while i<top:
		print "At the top i is %d" % i
		numbers.append(i)

		# no need if for-loop
		i = i + step
		print "numbers now:", numbers
		print "At the bottom i is %d" %i
	pass

numbers = []
top = 5 
step = 2

loop_function(numbers, top, step)

print "The numbers:"

for num in numbers:
	print num

