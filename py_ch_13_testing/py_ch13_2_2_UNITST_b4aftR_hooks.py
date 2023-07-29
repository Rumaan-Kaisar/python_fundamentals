
# Courses: colt_py_bootcamps    300

# -----------------------    Before and After Hooks    -----------------------
# Useful for testing larger applications:
    # sometimes we need some code to run 'before-test' and 'after-test'

    # Whether adding new data to database
    # creating fake data to use in testing:
        # creating fake user account

# Instead of creating all of these repeatedly to use everywhere, we can use "setUp" and "tearDown"


# -----------------------    setup and tearDown    -----------------------
    # setUp:
    # For larger applications, you may want similar code/application state before running tests
        # we put these in setUp, and it runs before every test metods
        # 'setUp' runs before 'EACH' test method

    # tearDown:
    # Similarly if we want a code to run after all of our tests, we use tearDown
        # testing DATABASE:
        # add data for testing, use "tearDown" to remove all the test data
        # 'tearDown' runs AFTER each test method
        # Common use cases: 
            # adding/removing data from a test DATABASE, 
            # creating instances of a class

    # since we're not using databases, we only focus on "setUp"
        # It's same as setUp(), and it runs after each of the test-function




# Example: Following is a demo code. 
    # "setUp" runs before 'test_first' and 'test_second'
    # "tearDown" runs after 'test_first' and 'test_second'

import unittest

class SomeTests(unittest.TestCase):
    def setUp(self):
        # do setup here 
        pass

    def test_first(self):
        # setup runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setup runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do teardown here
        pass




# Example 1: Following we have a 'robot-app' we named the file: 'robot.py'
                # and we also have 'robot_test.py' to test the 'robot-app'

# robot.py
    # each robot class have: name, battery, skill
    # charge() charges the battery
    # say_name() tells the name, and discharge the battery
    # learn_skill() learns a skill (append to a list), and discharge the battery
class Robot:
	def __init__(self, name, battery=100, skills=[]):
		self.name = name
		self.battery = battery
		self.skills = skills

	def charge(self):
		self.battery = 100
		return self

	def say_name(self):
		if self.battery > 0:
			self.battery -= 1
			return f"BEEP BOOP BEEP BOOP.  I AM {self.name.upper()}"
		return "Low power.  Please charge and try again"

	def learn_skill(self, new_skill, cost_to_learn):
		if self.battery >= cost_to_learn:
			self.battery -= cost_to_learn
			self.skills.append(new_skill)
			return f"WOAH. I KNOW {new_skill.upper()}"
		return "Insufficient battery. Please charge and try again"



# --------------    without "setUp"    --------------

# robot_test.py
    # following code tests the above app.


# following code tests the "robot.py" app.

import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    mega_man = Robot("Mega man", battery = 50)  # creating a Robot object

    def test_charge(self):
        mega_man = Robot("Mega man", battery = 50)  # creating a Robot object
        mega_man.charge()   # increase charge 50 to 100
        self.assertEqual(mega_man.battery, 100)

    def test_say_name(self):
        mega_man = Robot("Mega man", battery = 50)  # creating a Robot object again
        self.assertEqual(mega_man.say_name(), "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")    # string needs to be exact same
        self.assertEqual(mega_man.battery, 49)      # charg was 50 when the object was created
        

if __name__ == "__main__":
    unittest.main()


# Notice that we have to define the Robot object multiple time.
    # To avoid this duplication, we can use "setUp"

# Note: we can define one Robot object, at the biggining of the class,
""" 
    class RobotTests(unittest.TestCase):
         mega_man = Robot("Mega man", battery = 50)  # creating a Robot object

        def test_charge(self):
 """
    # But the issue is: During test, this single object is being manipulated multiple time
    # so using setUp is a good idea: it creates Robot object 'for each' test function


# --------------    above code using 'setUp()'    --------------
import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega man", battery = 50)  # creating a Robot object

    # Now we just referance the above object
    def test_charge(self):  
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.mega_man.say_name(), "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")    # string needs to be exact same
        self.assertEqual(self.mega_man.battery, 49)
        

if __name__ == "__main__":
    unittest.main()


# python robot_test.py





# robot_test.py
    # following code tests the above app.
    # notice the use of "setUp()"
        # it runs before "EACH METHOD": 'test_charge()' and 'test_say_name()'

# without "setUp"
import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()  # increase charge 50 to 100
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()




