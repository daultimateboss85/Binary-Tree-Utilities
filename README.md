# Binary Tree Utilities

### Description: Group of functions that help when working with binary trees

### Background To project

Binary Tree Utilities was a project inspired by me solving some binary tree problems. I realised i will be able to understand the problems better if i could somehow visualise the tree. This led me to try creating a function whose purpose was to print out a binary tree.
In my quest to do so, i created several functions relating to binary trees, and as such Binary Tree Utilitites was born.

### Node Representation

Nodes are intialised with the following call:

`node = Node(value, left, right)`

Where value is the value of the node, left is a pointer to the left child node and right a pointer
to the right child node. `left` and `right` should be node instances or `None` else a `ValueError` is raised.

### Main Features

- ### Get maximum depth of tree - `get_max_depth(root)`

  Given the root of a binary tree this function allows to get the maximum depth of a tree.
  Returns a tuple with item at first index being one leaf node with maximum depth and item at second index being an integer representing maximum depth of tree

  eg Calling `get_max_depth(Tree)` where Tree is below returns `(d, 3)`

  ```
         a
       /   \
     b       c
    / \     / \
   d   e   f   g
  ```

- ### Get nodes in tree by level - `get_nodes_bylevel(root, level)`

  Supplying a level and this function returns a list of all nodes on that level of the tree
  where the root node is level 1
  eg Calling `get_nodes_bylevel(Tree, 2)` on Tree below returns `[d, e, f ,g]`

  ```
        a
      /   \
    b       c
   / \     / \
  d   e   f   g
  ```

- ### Invert tree - `invert(root)`

  Given the root node to a binary tree, this function inverts the tree eg.
  With tree, Tree:

  ```
        a
      /   \
    b       c
   / \     / \
  d   e   f   g
  ```

  `invert(Tree)` Returns

  ```
        a
      /   \
    c       b
   / \     / \
  g   f   e   d
  ```

- ### Print tree - `print_bintree(root)`

  Given the root node to a binary tree, this function returns string representation of the tree which can then be printed. This string is well spaced and allows for easy visualizations of the workings on a binary tree.

  The following trees displayed are the output of the function when called on various trees
  (see nodes.txt. Trees displayed are a1, a2, a3 respectively).

  ```
        a
      /   \
    b       c
   / \     / \
  d   e   f   g

                a
            /       \
        b               c
      /   \           /   \
    d       e       f       g
   / \     / \     / \     / \
  h   i   j   k   l   m   n   o

                                a
                        /               \
                b                               c
            /       \                       /       \
        d               e               f               g
      /   \           /   \           /   \           /   \
    h       i       j       k       l       m       n       o
   / \     / \     / \     / \     / \     / \     / \     / \
  p   q   r   s   t   u   w   x   y   z   A   B   C   D   E   F
  ```

  For large trees the spacing at the top is a bit much, however with all trees the spacing allows for easy visualization of trees.

  PS: It is recommended to not use characters that are longer than 4 digits for the best display.

- ### Tree Traversals

  ```
       a1
      /   \
    b       c
   / \     / \
  d   e   f   g
  ```

  - #### Inorder traversal - `inorder_traversal(tree)`

    Returns the inorder traversal of a tree

    When called on tree above returns

    `[d, b, e, a1, f, c, g]`

  - #### Preorder traversal - `preorder_traversal(tree)`

    Returns the preorder traversal of a tree

    When called on tree above returns

    `[a1, b, d, e, c, f, g]`

  - #### Postorder traversal - `postorder_traversal(tree)`

    Returns the postorder traversal of a tree

    When called on tree above returns

    `[d, e, b, f, g, c, a1]`
