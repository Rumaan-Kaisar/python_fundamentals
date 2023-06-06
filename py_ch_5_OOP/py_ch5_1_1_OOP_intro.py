
# Courses: colt_py_bootcamps    232, 233

# Objectives:
    # Define OOP
    # Understand ENCAPSULATION & POLYMORPHISM
    # Create CLASS & INSTANCES and attach methods and properties to them


# ------------    OOP    ------------    
    # OOP is a method to model some process or thing in the real world as class or object

# ---------    class & instances    ---------
# Class
    # bluprient - contains METHODS (functions) and ATTRIBUTES (similar to keys in dict)

# instance
    # objects that are constructed from a class that contains their class's method and properties


# int, list, all those are actually "objects"
    # use "help()" to retrive documentation of Python
        # help() provides all sort of infromation including all "class-methods"
    # for example: "list" is a class and "num = [1, 2, 3]" is a INSTANCE of the 'list-class'




# ------------------    Abstruction & Encapsulation    ------------------
# The goal of OOP is ENCAPSULATE our codes into logocal, hierarchical grouping using classes 
    # it all about ORGANIZING and REUSING our codes
    # get rid of SPAGETTI CODE
    



# ---------    Example
# we want to model a game of poker in our program. We could have the following entities:
    # Game
    # Player
    # Card
    # Deck
    # Hand
    # Chip
    # Bet

    # then we can have the following methods/properties to build a "Deck - class"
""" 
                Deck {class}

        Card Deck Possible Implementation (Pseudocode)
        _cards          {private list attribute} 
        _max_cards      {private int attribute} 
        shuffle         {public method}
        deal_card       {public method}
        deal_hand       {public method}
        count           {public method}

 """

# Note about "Private" & "Public" 
    # Actually there is no such thing in Python, its just a covention to follow
    # "_name" means 'treat it as a private'



# ---------    Encapsulation    ---------
# Encapsulation - the grouping of 'public' and 'private' attributes and methods into a programmatic class, making abstraction possible
    # Example
        # Designing the Deck class, I make 'cards' a private attribute (a list)
        # I decide that the 'length of the cards' should be accessed via a 'public' method called" count()" -- i.e. "Deck.count()"



# ---------    Abstraction    ---------
# Abstraction is used to hide the 'internal functionality' of the function from the users. 
    # The users only interact with the basic implementation of the function, but inner working is hidden. 
    # User is familiar with that "what function does" but they don't know "how it does."

    # In simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., 
    # but we don't know how these operations are happening in the background.



# sometimes in OOP, we have to write more codes, but the code becomes more managable

