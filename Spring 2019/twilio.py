
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    
def __repr__(self):
        args = repr(self.value)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

def print(self):
        def print_helper(tree, depth):
            if tree.right:
                print_helper(tree.right, depth + 1)
            print("{0}{1}".format("\t" * depth, tree.value))
            if tree.left:
                print_helper(tree.left, depth + 1)
        print_helper(self, 0)

# 
#Your previous Python 2 content is preserved below:

def array_to_tree(arr, i):
    """
    Input: 
    [7, 3, 9, 2, 4, 8, 10]

    Output:
         7
       /   \
      3     9
     / \   / \
    2   4 8  10
    
    @type    arr: An array of integers
    @param   arr: An array of integers representing a balanced binary tree
    @rtype:  Binary tree's root node
    @return: A binary tree transformed from the input array
    """
    #pass
    
    if i > len(arr):
        return None
    
    root = Tree(arr[0])
    
    root.left = array_to_tree(arr[i*2 +1])
    
    root.right = array_to_tree(arr[i*2 +2])
    
    return root



result = array_to_tree([7, 3, 9, 2, 4, 8, 10])
        
result.print()