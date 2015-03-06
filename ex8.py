# -- coding: utf-8 --

formatter = "%r %r %r %r"
mandarin_formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right,",
	"But it did no't sing.",
	"So I said goodnight."
)

print mandarin_formatter % ("león", "您好", "马", "bye")
print u'哈哈'.encode('utf-8')