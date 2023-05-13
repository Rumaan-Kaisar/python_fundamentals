# Courses: colt_py_bootcamps    197, 


# -------------------    len()    -------------------
# Returns length (number of items) of an object
# argument may be sequence (string, tuple, list or range) or a collection (dictionary, set)

len("awesome")      # string
len([1,2,3,4,5,6])  # list
len((1,2,3,4,5,6))  # tuple
len(range(0, 10))   # range

len({1,2,3,4,5,6,7})    # set
len({"a":1, "b":2, "c":3})    # dictionary




# -------------    how its work?    --------------
# there is a __len__() method for all sequence and collection 
    # i.e. a string, list, tuple or dictionary already has this __len__() by their creation
    # behind the scene 'len()' is actually calling '_len_()'
"hello".__len__()   # 5, works the same way as len()




# -------------    User defined __len__()    --------------
# In OOP we can define our own version of __len__(), and we can call len() on our object


# Example 1: notice in the following class definition we are creating __len__()
class SpecialList:
 
    def __init__(self, data):
        self.__data = data
 
    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50


 
