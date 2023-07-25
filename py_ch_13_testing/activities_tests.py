
# ---------    This is TEST    ----------  
# We use following code to test "activities.py" app

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
