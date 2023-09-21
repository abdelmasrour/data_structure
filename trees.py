class Node:
    def __init__(self, key):
        self.key = key
        self.child = []
  
# Utility function to create a new tree node
def new_node(key):
    temp = Node(key)
    return temp
  
# Function that will return the depth
# of the tree
def depth_of_tree(ptr):
    # Base case
    if ptr is None:
        return 0
  
    # Check for all children and find
    # the maximum depth
    maxdepth = 0
    for child in ptr.child:
        maxdepth = max(maxdepth, depth_of_tree(child))
  
    return maxdepth + 1
  
# Driver program
if __name__ == '__main__':
    """ Let us create below tree
            A
          / \ 
         F   E
        / \    \
        K  J    I
        /\        \
        N  M        L
    """
  
    root = new_node('A')
    root.child.extend([new_node('F'), new_node('E')])
    root.child[0].child.extend([new_node('K'), new_node('J')])
    root.child[1].child.append(new_node('I'))
    root.child[0].child[0].child.extend([new_node('N'), new_node('M')])
    root.child[1].child[0].child.append(new_node('L'))
  
    print(depth_of_tree(root))
