from sys import argv

script, filename = argv

print "Let's read that file!it says:"
target = open(filename);
print target.read()
target.close()

print "and let's add a comment to the end."
new_line = raw_input("w:")
new_line = "\n"+new_line

target = open(filename, 'a+');
target.write(new_line)
target.close()
print("packed and shipped!")

