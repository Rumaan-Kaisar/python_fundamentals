
# Courses: colt_py_bootcamps    293, 294

# ------------------    TESTING    ------------------
# Story of testing:
# Test Driven Development: TDD
# Syntax of TESTING
# writing our own test

# Example of TEST: same thing in "Different Variety" using assertions



""" 
    =============    OBJECTIVES    =============
    # Describe what tests are and why they are essential
    # Explain what Test Driven Development (TDD) is
    # Test Python code using DOCTESTS
    # Test Python code using ASSERT
    # Explain what UNIT TESTING is
    # Write "unit tests" using the "unittest" module
    # Remove 'code duplication' using before and after hooks
"""




# ------------------    why testing matters?    ------------------
# To Reduce BUGS in our codes
# Ensure bugs that are solved stay solved: 
    # Find a BUG earlier, when added new code to a Corrected-code
# Ensure that new features doesn't break old ones (kind of main reason).   
# Ensure that Refactoring/Clean-up codes doesn't introduce new bugs
# For large-scale development (for a client) "TESTING" is a must do 



# ---------------    TDD - Test Driven Development    ---------------
# Testing is, writing some codes that tests other code
# you can test any point
    # After creating a new function
    # After writing entire application
    # Or, use TDD

    # TDD method:
        # Development begins by writing TESTS
        # Once tests are written, write code to make tests PASS
        # Once tests pass, a feature is considered COMPLETE



# ----------------    RED, GREEN, REFACTOR    ----------------
# these are the color that a code passing or failing

# It is a workflow of TDD:
    # 1.	Red     - Write a test that FAILS
    # 2.	Green   - Write the minimal amount of code necessary to make the test PASS
    # 3.	Refactor - Clean up the code, while ensuring that tests STILL PASS

