import random
def eat(food, is_healthy):
    # raise 'Value ERR' for is_healthy
    if not isinstance(is_healthy, bool) :
        raise ValueError("Must be a Boolean")

    ending = "because YOLO!"
    # make different ending if is_healthy=True    
    if is_healthy:
        ending = "it makes my bdy a Tmpl"
        
    return f"I'm eating {food}, {ending}"

def nap(no_of_hours):
    if (no_of_hours >= 2):
        return "Ugh I overslept!"
    else:
        return "Felling Good!"

# -------   new code   -------
def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return random.choice(('lol', 'haha', 'tehehe'))