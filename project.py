class Node():
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
            taketwo += f"{node.__str__() : ^{divisions_space}}"
        
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

def inorder_traversal(root, current=None):
    if current is None:
        current = []

    if not root:
        return []
    
    if not root.left and not root.right:
        return [root]
    
    else:
        current.extend(inorder_traversal(root.left))
        current.append(root)
        right = inorder_traversal(root.right )
        current.extend(right)

        return current

def preorder_traversal(root, current=None):
    if current is None:
        current = []

    if not root:
        return
    
    if not root.left and not root.right:
        return [root]
    

    else:
        current.append(root)
        current.extend(preorder_traversal(root.left))
        current.extend(preorder_traversal(root.right))

        return current
    
def postorder_traversal(root, current=None):
    if current is None:
        current = []
    
    if not root:
        return
    
    if not root.left and not root.right:
        return [root]
    
    else:
        current.extend(postorder_traversal(root.left))
        current.extend(postorder_traversal(root.right))
        current.append(root)

        return current


def main():
    g = Node("g",)
    f = Node("f", )
    d = Node("d",)
    e = Node("e",)
    c = Node("c", f, g)
    b = Node("b", d, e)
    a1 = Node("a1", b, c) 

    o = Node("o")
    n = Node("n")
    m = Node("m")
    l = Node("l")
    k = Node("k")
    j = Node("j")
    i = Node("i")
    h = Node("h")
    g = Node("g", n, o)
    f = Node("f", l, m)
    d = Node("d",h,i)
    e = Node("e", j, k)
    c = Node("c", f, g)
    b = Node("b", d, e)
    a2 = Node("a2", b, c) 

    p = Node("p")
    q = Node("q")
    r = Node("r")
    s = Node("s")
    t = Node("t")
    u = Node("u")
    v = Node("v")
    w = Node("w")
    x = Node("x")
    y = Node("y") 
    z = Node("z")
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E") 
    F = Node("F")
    o = Node("o", E, F)
    n = Node("n", C, D)
    m = Node("m", A, B)
    l = Node("l", y, z)
    k = Node("k", w, x)
    j = Node("j" ,t, u)
    i = Node("i", r, s)
    h = Node("h", p, q)
    g = Node("g", n, o)
    f = Node("f", l, m)
    d = Node("d",h,i)
    e = Node("e", j, k)
    c = Node("c", f, g)
    b = Node("b", d, e)
    a3 = Node("a3", b, c)

    tree = a2

    print(f"Printing tree {tree}")
    print(print_bintree(tree))

    print()
    print(f"Max depth of {tree}: {get_max_depth(tree)}")

    print(f"Nodes on 3rd level of {tree}: {get_nodes_bylevel(tree, 3)}")

    print()
    print(f"Inorder traversal of {tree}: ",end ="")
    print(inorder_traversal(tree))

    print("Preorder:", end=" ")
    print(preorder_traversal(tree))

    print("Postorder:", end=" ")
    print(postorder_traversal(tree))

    print("\n")
    
    print(f"Inverting {tree}: ")
    invert(tree)
    print(print_bintree(tree))

if __name__ == "__main__":
    main()
