
# Courses: colt_py_bootcamps    300

# -----------------------    Before and After Hooks    -----------------------



# -----------------------    setup and tearDown    -----------------------

    # For larger applications, you may want similar application state before running tests
    # 'setUp' runs BEFORE each test method
    # 'tearDown' runs AFTER each test method
    # Common use cases: adding/removing data from a test database, creating instances of a class



# Example:
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




# Example :
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



