# class Thing {
#   String name;
#   List<Thing> things;
# }
# Make a deep copy of an instance for this strucuture

# print("Hello World")

#A [B, C]
#B [A]
#C []

class Thing:
    def __init__(self, name):
        self.name = name
        self.lst = []
        
    

def copy(thing, set_things):
    
    if thing in set_things:
        return thing
    
    new_copy = Thing(thing.name)
    set_things.add(thing)
    
    new_lst = []
    
    for i in thing.lst:
        new_lst.append(copy(i, set_things))
        
    new_copy.lst = new_lst
    
    
    return new_copy