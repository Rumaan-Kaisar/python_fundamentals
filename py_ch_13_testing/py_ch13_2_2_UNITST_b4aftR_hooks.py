
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

    3:10    













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
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()




""" 
    Example : Your goal in this assignment will be to add tests to the classes you created in the last section: Card  and Deck . 
                    Try to test that instances have the right structure, and write some tests for the methods. 
                    Use some before hooks, and try to test for expected errors as well!

                    Note that the shuffle  method will be difficult to test, since it produces a random output. 
                        Rather than trying to test randomness, you may just want to write some smaller, more straightforward tests. 
                        For instance, you could test that shuffle  doesn't change the size of the deck, or 
                        that the list of cards before the shuffle is in a different order than after the shuffle. 
"""



