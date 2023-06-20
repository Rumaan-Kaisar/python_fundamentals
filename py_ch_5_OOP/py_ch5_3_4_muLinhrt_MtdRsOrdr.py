
# Courses: colt_py_bootcamps    258, 259

# ------------    Multiple inheritance    ------------

class Aquatic:
  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name

  def swim(self):
    return f"{self.name} is swimming"

  def greet(self):
    return f"I am {self.name} of the sea!"



class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name

  def walk(self):
    return f"{self.name} is walking"

  def greet(self):
    return f"I am {self.name} of the land!"


# Ineherit from two different classes 
  # just specify the parent classes in the argument
  # Ambulatory, Aquatic are two different classes they have no relation
  # But "Penguin" has relation to both classes

# class Penguin(Aquatic, Ambulatory):
class Penguin(Ambulatory, Aquatic):  
  def __init__(self,name):
    print("PENGUIN INIT!")
    # Aquatic's __init__() never caled if super().__init__ is ussed
      # But because of the inheritance we have acces to the other methods of both parent classes
    super().__init__(name=name) # if class is unspecified MRO applied

    # for the above reason we can explicitky call the __init__ of each parent calsses
      # However "greet" is invoked from "Ambulatory"
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)



jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
# note that when class_name is unspecified and super().__init__ is used
  # first of the specified base's method will be used (in case both class has same method_name)
  # i.e Aquatic, Ambulatory both has "greet()"
    # in case of "class Penguin(Aquatic, Ambulatory)" Aquatic's "greet" wil be used
    # in case of "class Penguin(Ambulatory, Aquatic)" Ambulatory's "greet" wil be used
print(captain_cook.greet())

# followig shows "captain_cook" is the instance of all three classes 'Penguin', 'Aquatic' and 'Ambulatory'
print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")





# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'

# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??


# python py_ch5_3_4_muLinhrt_MtdRsOrdr.py

