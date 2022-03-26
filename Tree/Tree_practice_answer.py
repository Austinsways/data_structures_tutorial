"""this is the BST class we will be using."""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

         
    def __iter__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a loop
        is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
        use.  When the 'for' loop wants to get the next value, the code in
        this function will start back up where the last 'yield' returned a 
        value.  The keyword 'yield from' is used when we want to 'yield' a
        value that is returned from a function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    #problem 3
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)  # Replace this when you implement your solution
    
    #problem 4
    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """    
        return self._find(data, self.root)  # Start at the root

    def _find(self, data, node):
        #you need to use recursion to find the value. 
        if data == node.data:
            return True
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                pass
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                pass
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                return self._find(data, node.right)
    


#lets take some values and use a BST to store and find them.
numbers_to_store = [2,3,5,6,87,9,9,8,6,5,4,3,32,2,3,45,5,6,77,88,7,65,4,3,2,11,1,2,3,4,4,56,6,88,8,8,63,3,44,3,3,2]

#start by creating a BST 
our_tree = BST()

#now lets add all the numbers to the BST (please write a for loop instead of hard coding)
for number in numbers_to_store:
    our_tree.insert(number)

#write a function to traverse backwards through the BST, from greates to smallest. write this method using the _traverse_backwards function
for x in reversed(our_tree):
    print(f"{x},", end="")  
print()

#write a function to traverse the BST to find if the value 88 is present. use the __contains__ method inside of the BST class, and write the _find method.
if 88 in our_tree:
    print("Found 88!")
else:
    print("88 not found")
