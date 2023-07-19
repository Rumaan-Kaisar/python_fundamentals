
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


