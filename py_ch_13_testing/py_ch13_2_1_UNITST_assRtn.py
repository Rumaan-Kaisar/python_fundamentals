
# Courses: colt_py_bootcamps    298, 299

# ------------    uniTTest    ------------
# Unit test is the builtin module for testing

# Idea of Unit Testing:
    # Test the smallest pices: Smallest pices are called "units"

    # We do not test the entire application in one go
        # we focus on small units
    
    # Test smallest parts of an application in isolation (e.g. units) 
    
    # Good candidates for unit testing: 
        # individual classes, 
        # modules, or 
        # functions
    
    # Bad candidates for unit testing: 
        # an entire application, 
        # dependencies across several classes or 
        # modules

# unittest is a framework:
    # There is a documentation and different parts
    # assertions: for now we'll focus on "assertions"
        # there are builtin assertions that we can run
        # for example: These are self explanetory

""" 
            assertEqual(a, b) 
            assertNotEqual(a, b) 
            assertTrue(x) 
            assertFalse(x) 
            assertIs(a, b) 
            assertIsNot(a, b) 
            assertIsNone(x) 
            assertIsNotNone(x)

            assertIn(a, b)
            assertNotln(a, b)
            assertIsInstance(a, b) 
            assertNotIsInstance(a, b) 
"""




# ------------    unittest    ------------
    # Python comes with a built-in module called "unittest" 
    # You can write unit tests encapsulated as classes that inherit from 'unittest.TestCase' 
    # This inheritance gives you access to many 'assertion helpers' that let you test the behavior of your functions 
    # You can run tests by calling unittest.main())




# Example 1: lets say 'activities.py' is our app.
            # For unittest, we have another file called "tests.py"

# ********    'activities.py'    ********:
def eat(food, ishealthy): 
    pass

def nap(num_hours): 
    pass


# ***********    "tests.py"    ***********:
import unittest     
from activities import eat, nap     #  load functionality fronm the app that we want to test

# the name "ActivityTests" could be anything, but it needs to "INHERIT" from 'unittest.TestCase'
class ActivityTests(unittest.TestCase):
    pass

# finally following runs our tests
if __name__ == "__main__" :
    unittest.main()


# Using TDD method, we'll modify 'activities.py'
    # To do that, first we need to setup unittest in "test.py"
    # we run the "tests.py" and then modify the app to pass the failed tests



# ============= ATTEMPT 1:
# in activities.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities.py

def eat(food, is_healthy):
    pass

def nap(no_og_hours):
    pass



# in tests.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

if __name__ == "__main__": 
    unittest.main()

# try to run tests.py

""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py
F
======================================================================
FAIL: test_eat (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 7, in test_eat
    self.assertEqual(eat("broccoli", is_healthy=True), "My bdy is a Tmpl")
AssertionError: None != 'My bdy is a Tmpl'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
"""




# ============= ATTEMPT 2:
# in activities.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities.py

def eat(food, is_healthy):
    ending = "because YOLO!"
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    pass



# Note: We cannot have multple assertions in one test as below:

# class ActivityTests(unittest.TestCase):
#     def test_eat(self):
#         self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
#         self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

# EACH assertion needs its own function for testing




# ============= ATTEMPT 3:
# in activities.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities.py

def eat(food, is_healthy):
    ending = "because YOLO!"
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    pass



# in tests.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
    
    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

if __name__ == "__main__": 
    unittest.main()

# try to run tests.py
# Now we've got 2 tests and 1 failure
""" 
F.
======================================================================
FAIL: test_eat_healthy (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 7, in test_eat_healthy
    self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
AssertionError: "I'm eating broccoli, because YOLO!" != "I'm eating broccoli, it makes my bdy a Tmpl"
- I'm eating broccoli, because YOLO!
+ I'm eating broccoli, it makes my bdy a Tmpl


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
"""




# ============= ATTEMPT 4:
# in activities.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities.py

def eat(food, is_healthy):
    ending = "because YOLO!"
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    pass



# in tests.py, we now add two more tests for nap()
# H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
    
    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Ugh I overslept!")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py
# Now we've got 4 tests and 3 failure
# Notice the "F.FF", "." for pass, "F" for fail
""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py
F.FF
======================================================================
FAIL: test_eat_healthy (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 7, in test_eat_healthy
    self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
AssertionError: "I'm eating broccoli, because YOLO!" != "I'm eating broccoli, it makes my bdy a Tmpl"
- I'm eating broccoli, because YOLO!
+ I'm eating broccoli, it makes my bdy a Tmpl


======================================================================
FAIL: test_long_nap (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 17, in test_long_nap
    self.assertEqual(nap(3), "Ugh I overslept!")
AssertionError: None != 'Ugh I overslept!'

======================================================================
FAIL: test_short_nap (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 14, in test_short_nap
    self.assertEqual(nap(1), "Felling Good!")
AssertionError: None != 'Felling Good!'

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=3)
"""




# ============= ATTEMPT 5:
# in activities.py
# H:\shared_docs\codes_py\py_ch_13_testing\activities.py

def eat(food, is_healthy):
    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"



# in tests.py, we now add two more tests for nap()
# H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
    
    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy="True"), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Ugh I overslept!")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py
# Now we've got 4 tests and 1 failure
# Notice the ".F..", "." for pass, "F" for fail
""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py
.F..
======================================================================
FAIL: test_eat_unhealthy (__main__.ActivityTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 11, in test_eat_unhealthy
    self.assertEqual(eat("pizza", is_healthy="True"), "I'm eating pizza, because YOLO!")
AssertionError: "I'm eating pizza, it makes my bdy a Tmpl" != "I'm eating pizza, because YOLO!"
- I'm eating pizza, it makes my bdy a Tmpl
+ I'm eating pizza, because YOLO!


----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
"""




# ============= ATTEMPT 6 (final):
# in activities.py
def eat(food, is_healthy):
    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"



# in tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")
    
    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        self.assertEqual(nap(3), "Ugh I overslept!")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py: python activities_tests.py
# Notice "....", all test passed
""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
"""




# -----------------    COMMENTING the Tests    -----------------

# Previously, if all the tests passed, we've not much info, so adding comment is helpful
    # We'll add "DOCSTRINGS" to our "TEST-FUNCTIONS"
    # To see the comments, we run in CLI :

        #   python name_of_test_file.py -v
        #   python activities_tests.py -v

""" 
    test_eat_healthy (__main__.ActivityTests) ... ok
    test_eat_unhealthy (__main__.ActivityTests) ... ok
    test_long_nap (__main__.ActivityTests) ... ok
    test_short_nap (__main__.ActivityTests) ... ok
"""


# in activities.py
def eat(food, is_healthy):
    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"



# in tests.py
import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")

    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        """eat should indicate you've given up for eating unhealthy"""
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(nap(3), "Ugh I overslept!")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py: python activities_tests.py -v

""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py -v
test_eat_healthy (__main__.ActivityTests)
eat should have a positive message for healthy eating ... ok
test_eat_unhealthy (__main__.ActivityTests)
eat should indicate you've given up for eating unhealthy ... ok
test_long_nap (__main__.ActivityTests)
long naps should be discouraging ... ok
test_short_nap (__main__.ActivityTests)
short naps should be refreshing ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.006s

OK
"""




# -----------------    Other UNITTEST asstertions    -----------------
# following are some common types of assertions of unittest

            # assertEqual(a, b) 
            # assertNotEqual(a, b) 
            # assertTrue(x) 
            # assertFalse(x) 

            # assertIsNone(x) 
            # assertIsNotNone(x)
            # assertIn(a, b)
            # assertNotln(a, b)

# cosider following example

# in activities.py
def eat(food, is_healthy):
    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"

# -------   new code   -------
def is_funny(person):
    pass


# in tests.py
import unittest
from activities import eat, nap, is_funny

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")

    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        """eat should indicate you've given up for eating unhealthy"""
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(nap(3), "Ugh I overslept!")

    # new codes
    def test_is_funny_tim(self):
        """ Is tim funny? """
        # self.assertEqual(is_funny("tim"), False)
        # or we can use following
            # Note: we can use message as argumnet
        self.assertNotEqual(is_funny("tim"), "tim should not be funny!")

        # Note: These are actually a little bit different. 
            # 'assertFalse', 'assertNotEqual' are checking for 'False-y values', not just "False".

    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py: python activities_tests.py -v

""" 
H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py -v
test_eat_healthy (__main__.ActivityTests)
eat should have a positive message for healthy eating ... ok
test_eat_unhealthy (__main__.ActivityTests)
eat should indicate you've given up for eating unhealthy ... ok
test_is_funny_anyone_else (__main__.ActivityTests)
anyone else but tim should be funny ... FAIL
test_is_funny_tim (__main__.ActivityTests)
Is tim funny? ... ok
test_long_nap (__main__.ActivityTests)
long naps should be discouraging ... ok
test_short_nap (__main__.ActivityTests)
short naps should be refreshing ... ok

======================================================================
FAIL: test_is_funny_anyone_else (__main__.ActivityTests)
anyone else but tim should be funny
----------------------------------------------------------------------
Traceback (most recent call last):
  File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 36, in test_is_funny_anyone_else
    self.assertTrue(is_funny("blue"), "blue should be funny")
AssertionError: None is not true : blue should be funny

----------------------------------------------------------------------
Ran 6 tests in 0.011s

FAILED (failures=1)
"""


# Notice: there is one failure,

    # Because, 'assertNotEqual' is checking for 'False-y values', and "None" is a fals-y value
    # if we use "assertEqual", we'll get following messages with 2-failures
        # Notice: "AssertionError: None != False"
        # Hence 'assertEqual' is more safer


# H:\shared_docs\codes_py\py_ch_13_testing>python activities_tests.py -v
#             --------
#             --------
#             --------

# ======================================================================
# FAIL: test_is_funny_tim (__main__.ActivityTests)
# Is tim funny?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "H:\shared_docs\codes_py\py_ch_13_testing\activities_tests.py", line 26, in test_is_funny_tim
#     self.assertEqual(is_funny("tim"), False)
# AssertionError: None != False

# ----------------------------------------------------------------------
# Ran 6 tests in 0.002s

# FAILED (failures=2)




# Now lets correct activities.py
def eat(food, is_healthy):
    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"

# -------   new code   -------
def is_funny(person):
    if person is "tim": return False
    return True

# No FAILOURES
# ----------------------------------------------------------------------
# Ran 6 tests in 0.001s

# OK





# ------------------    more Assertions    ---------------------
# Use randon values in an "assertion"
    # self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


# ----------------    Testing for Errors    -------------------
# Use to ensure the occurence of certain "ERR" and "ERR-type"
# ERR handling with assertion, use following pattern
class SomeTests(unittest.TestCase): 
    def testing_for_error(self):
        """ testing for an error """
        with self.assertRaises(IndexError): 
            ls = [1, 2,3]
            ls[100]



# in activities.py
import random
def eat(food, is_healthy):
    # raise 'Value ERR' for is_healthy
    if not isinstance(is_healthy, bool) :
        raise ValueError("Must be a Boolean")

    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"

# -------   new code   -------
def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return random.choice(('lol', 'haha', 'tehehe'))



# in tests.py
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(eat("broccoli", is_healthy=True), "I'm eating broccoli, it makes my bdy a Tmpl")

    # EACH assertion needs its own function for testing
    def test_eat_unhealthy(self):
        """eat should indicate you've given up for eating unhealthy"""
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO!")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(nap(1), "Felling Good!")

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(nap(3), "Ugh I overslept!")

    # new codes
    def test_is_funny_tim(self):
        """ Is tim funny? """
        self.assertEqual(is_funny("tim"), False)
        # or we can use following
            # Note: we can use message as argumnet
        # self.assertNotEqual(is_funny("tim"), "tim should not be funny!")

        # Note: These are actually a little bit different. 
            # 'assertFalse', 'assertNotEqual' are checking for 'False-y values', not just "False".

    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    # Use randon values in an "assertion"
    def test_laugh(self):
        """laugh returns a laughing string"""
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

    # ERR handling with assertion, it checks if the following ERR occurs
    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")


if __name__ == "__main__": 
    unittest.main()

# try to run tests.py: python activities_tests.py -v

# ----------------------------------------------------------------------
# Ran 8 tests in 0.010s

# OK
