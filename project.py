class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value}"
    
    def __str__(self):
        return f"{self.value}"
    
    
def invert(root):
    if not root.left and not root.right:
        return 
    
    else:
        if root.right:
            invert(root.right)
        if root.left:
            invert(root.left)

        root.left,root.right = root.right,root.left

        return


def get_max_depth(root):
    if not root:
        return (0, -1)

    elif not root.left and not root.right:
        return (root, 1)

    else:
        max_depth = max([get_max_depth(root.left), get_max_depth(root.right)], key=lambda x: x[1])
        return (max_depth[0], max_depth[1] + 1)


def get_nodes_bylevel(tree, level):
    #function that gets nodes from tree by level
    if level == 1:
        return [tree] 
    
    else:
        nodes = []
        nodes_from_left =  get_nodes_bylevel(tree.left, level-1)
        nodes_from_right = get_nodes_bylevel(tree.right, level-1)

        nodes.extend(nodes_from_left)
        nodes.extend(nodes_from_right)

        return nodes

def print_bintree(tree):
    #first determine max depth
    max_depth = get_max_depth(tree)[1]
   
    space_avalaible = 2**(max_depth+1) - 2
    
    #take 2 centering by 2 is divisions of space
    taketwo = ""
    for i in range(0, max_depth):
  
        nodes_at_level = get_nodes_bylevel(tree, i+1)

        divisions_space = space_avalaible // 2 ** i + 1
        
        for node in nodes_at_level:
            taketwo += f"{node.value : ^{divisions_space}}"
        
        #another take on slashes
        slashes = ""
        num_slashes = 2**(i+1) #slashes on next line

        if i != max_depth-1:
            taketwo += "\n"
            for j in range(num_slashes):
            
                div_space = space_avalaible // 2**(i+2) + 1

                if j % 2 == 0 :
                    to_add = "/"
                    slashes +=  " "*div_space + f"{ to_add: ^{div_space}}"
        
                else:
                    to_add = "\\"
                    slashes += f"{ to_add: ^{div_space}}" + " "*div_space

            taketwo += slashes + "\n"

    return taketwo
