def winner(votes):
    count = 0
    for v in votes:
        if v == '0':
            count += 1
        else:
            count -= 1
    
    if count == 0:
        return 'draw'
                
    if count > 0:
        return '0'
    
    return '1'
    

total = 0
def divisible(digit):
    total += digit
    total = total % 3
    
    if total == 0:
        return "Yes"
    
    return 'No'
    

// Write a function to find the minimum weight in a given binary tree, 
// where the weight of the tree is described as the sum of all its node weights, 
// and each node weight is described as the value of the node multiplied by its level.

// Time - O()
// Space - O()

def minWeight(bTree):
    getWeights(bTree, 1)
    
    getSums(bTree)
    
    
    


def getWeights(bTree, level):
    bTree.value *= level
    
    if bTree.left is None and bTree.right is None:
        return
    
    if bTree.left:
        getWeights(bTree.left, level + 1)
    
    
    if bTree.right:
        getWeights(bTree.right, level + 1)
        
def getSums(bTree):
    if bTree.left is None and bTree.right is None:
        return bTree.value
        
    if bTree.left:
        left = getSums(bTree.left)
        bTree.value += left
        
    if bTree.right:
        right = getSums(bTree.right)
        bTree.value += right
        
    return bTree.value
    

currMin = 0
def getMin(bTree):
    
    if bTree.left is None and bTree.right is None:
        return bTree
        

# ROOT
# |
# + A.txt 1kb
# + B.txt 2kb
# + C.pdf 100kb
# + D1
#   |
#   + A.txt 2kb
#   + B.pdf 50kb
#   + D11
#      |
#      ...
# ...
#
# - find all the files by their names: e.g find all the files with the name A -> List of all the files with the name A.
# - find all the files by their types: e.g find all the files with the type txt -> List of all the files with the type txt.
#
# File { 
#   name, type, size;
#   List<File> getAllFiles(Path path);
#   bool isDir();
#   Path getPath();
# }
#
class FindFiles: 
    
    def findFiles(name):
        
        return helper(name, 'Root', [], )
    
    def helper(name, path, result): 
        
        for file in getAllFiles(path):
            
            
            if file.isDir():
                findName(name, file.getPath, result)
            
            elif name == file.name:
                result += [file]                
        
        
        return result
        
        
class Matcher:
    @abstractmethod
    def match(file, string):
        pass

class NameMatcher(Matcher):
    
    def match(file, string):
        return file.name == string
        
 
    