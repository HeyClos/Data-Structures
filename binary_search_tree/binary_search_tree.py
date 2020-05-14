"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

class BSTNode:
    # this is a constructor
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # we need to change its neighbors references
        if value < self.value:
            if self.left is None:
                # this is my terminating condition because im not calling insert
                new_node = BSTNode(value)
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check to make sure right is empty, if so return self.value
        if self.right is None:
            return self.value
        else:
            # this is called a call stack!!!!!
            return self.right.get_max()

    # an iterative version of the method above
    def iterative_get_max(self):
        current_max = self.value

        current = self
        # travese our structure
        while current is not None: # we can also just say while current:
            if current.value > current_max:
                current_max = current.value
        # update our current_max variable if we see a larger value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        # pass fn to left child
        if self.left:
            self.left.for_each(fn)

        # pass fn to right child
        if self.right:
            self.right.for_each(fn)
        # note that we have a stack in the background here
        # note that we dont need to return anything
        # we just have to provide the structure for the incoming fn to run


    # Iterative version of the fn above
    def iterative_for_each(self, fn):
        stack = []

        # add the root node
        stack.append(self)

        # loop so long as stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            fn(current.value)
    # ^ Above is all Depth-First Traversal

    def breadth_first_for_each(self, fn):
        queue = deque()

        # add the root node
        queue.append(self)

        # loop so long as the stack still has elements 
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)
            
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
