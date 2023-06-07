
# Courses: colt_py_bootcamps    239

# -----------------    underscore '_' usage    -----------------
# _name: Makes no difference at all. Its just a convension for private variables.
        # There is no "public" or "private" in python

# __name: It has effect. Its called "Name mangling".
        # it is for "Inheritance" purpose.
        # any attribute with double undercore above it is concatenated with its "class", Eg: _class__name
            # so that no "Name conflict" will arise

# __name__: do not make __dunder__ for your own-fun, you may override predefined important methods of Python


# The dir() function returns all properties and methods of the specified object, without the values.


class Person:
    def __init__(self):
        self.name = "Tony" 
        self._secret = "hi!"
        self.__msg	= "I like turtles"  # name mangling
        self.__lol	= "HAHAHAHAH"   # name mangling

# 'name' and '_secret' both act same
p = Person()
print(p.name) 
print(p._secret)


print(dir(p))   # dir() function returns all properties
# ['_Person__lol', '_Person__msg', . . . , 'name']

print(p.__msg)  # won't work, we have to specify it's class
print(p.__lol)  # won't work, we have to specify it's class

# Following will work
print(p._Person__msg) 
print(p._Person__lol) 



#	def doorman(self, guess):
    #	if guess == self._secret:
    #	let them in