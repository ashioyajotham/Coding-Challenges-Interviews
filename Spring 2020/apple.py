def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

# C -> D
# A -> B, C (A depends on B & C),
# E
# D, E, B, C, A / E, D, C, B, A

#.  A      E
#. / \
# B  C
#    |
#.   D
def dependency(hashMap):
    
    result  = []
    while len(hashMap) != 0:
        
        remove = []
        for key in hashMap:
            if hashMap[key] == []:
                remove += [key]
            
        
        for key in hashMap:
            
            for r in remove:
                if r in hashMap[key]:
                    hashMap[key].remove(r)
                    
        for r in remove:
            result += [r]
            hashMap.remove(r)
        
        
    
    
    return result
    