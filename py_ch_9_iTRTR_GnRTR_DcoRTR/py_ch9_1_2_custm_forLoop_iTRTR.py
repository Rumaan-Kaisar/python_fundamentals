
# Courses: colt_py_bootcamps    267, 268


# -------------    Custom For Loop    -------------

# for num in [1,2,3]
# for char in "hi there"

def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)
		
def square(x):
	print(x*x)


my_for("lol", print)
my_for([1,2,3,4,5], square)





# -------------    Custom iterator    -------------
# it is kind of reverse of defining a custom-for loop (as above)
class Cuntr:
	def __init__(self, low, high):
		self.low = low
		self.high = high
		
	# we have to define __iter__() Dunder to make a iterator
	# __iter__ makes an iterable object
	def __iter__(self):
		return iter("hello")


# when 'for-loop' runs on "Cuntr", it will invoke __iter__()

for x in Cuntr(10, 20):
	print(x)




# To make above work properly, we need to return "self" from __iter__
	# we also need to define __next__() to make it a prper iterator
		# and raise "StopIteration" inside of it
class Cuntr:
	def __init__(self, low, high):
		self.low = low
		self.high = high
		
	# we have to define __iter__() Dunder to make a iterator
	# __iter__ makes an iterable object
	def __iter__(self):
		return self		# this actually invokes __next__()

	def __next__(self):
		# return 1	# makes infinite loop
		if self.low < self.high:
			num = self.low
			self.low += 1
			return num
		# we also need to raise the "StopIteration" ERR
		raise StopIteration


# when 'for-loop' runs on "Cuntr", it will invoke __iter__()

for x in Cuntr(1, 20):
	print(x)

# "Cuntr()" actually works like "range()"




# Example 1: Make our "Deck" class iterable
# to iterate over our cards we need to add folloing code in the "Deck" class
    # note that, we are not defining our own version of iterator (done above)
        #  we're just using iter() over 'self', so we don't need to define next()
def __iter__(self):
    return iter(self)


# python py_ch9_1_2_custm_forLoop_iTRTR.py

