import pytest
from project import Node, get_max_depth, get_nodes_bylevel, inorder_traversal, preorder_traversal, postorder_traversal

def test_instantiation():
    c = Node("c")
    b = Node("b")
    a = Node("a", b, c)

    assert isinstance(c, Node) == True
    assert isinstance(b, Node) == True
    assert isinstance(a, Node) == True

def test_badinstantiation():
    with pytest.raises(ValueError):
        c = Node("c", "a")
    with pytest.raises(ValueError):
        b = Node("b", 2)

    with pytest.raises(ValueError):
        a = Node("a",None, "")

def test_maxdepth():
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
    assert get_max_depth(a1)[1] == 3
    assert get_max_depth(a2)[1] == 4

def test_getnodesbylevel():
    g = Node("g",)
    f = Node("f", )
    d = Node("d",)
    e = Node("e",)
    c = Node("c", f, g)
    b = Node("b", d, e)
    a1 = Node("a1", b, c) 

    assert  get_nodes_bylevel(a1,2) == [b, c]
    assert  get_nodes_bylevel(a1,3) == [d, e, f, g]
    
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

    assert  get_nodes_bylevel(a2,1) == [a2]
    assert  get_nodes_bylevel(a2,3) == [d, e, f, g]


def test_traversal():
    g = Node("g",)
    f = Node("f", )
    d = Node("d",)
    e = Node("e",)
    c = Node("c", f, g)
    b = Node("b", d, e)
    a1 = Node("a1", b, c) 

    assert inorder_traversal(a1) == [d, b, e, a1, f, c, g]
    assert preorder_traversal(a1) == [a1, b, d, e, c, f, g]
    assert postorder_traversal(a1) == [d, e, b, f, g, c, a1]