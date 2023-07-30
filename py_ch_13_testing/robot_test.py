
# following code tests the "robot.py" app.

import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    mega_man = Robot("Mega man", battery = 50)  # creating a Robot object

    def test_charge(self):
        mega_man = Robot("Mega man", battery = 50)  # creating a Robot object
        mega_man.charge()
        self.assertEqual(mega_man.battery, 100)

    def test_say_name(self):
        mega_man = Robot("Mega man", battery = 50)  # creating a Robot object again
        self.assertEqual(mega_man.say_name(), "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")    # string needs to be exact same
        self.assertEqual(mega_man.battery, 49)
        

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


# above code using 'setUp()'
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
