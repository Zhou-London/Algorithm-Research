"""
Implementation of LLRB tree
"""


class RBNode:
    def __init__(self, val):
        self.val = val
        self.left: RBNode = None
        self.right: RBNode = None
        self.is_red = True


class LLRBTree:
    def __init__(self):
        self.root = None

    def check_red(self, node: RBNode):
        return node.is_red if node is not None else False

    def rotate_left(self, high: RBNode):

        # Rotate the nodes
        # right_ptr is a pointer to the right node of high
        # high's right child became right_ptr's left child
        # right_ptr's left child became high
        right_ptr = high.right
        high.right = right_ptr.left
        right_ptr.left = high
        # Now right_ptr is the highest node

        # Inherit the color
        right_ptr.is_red = high.is_red
        # Modify previous high's color
        high.is_red = True
        return right_ptr

    def rotate_right(self, high: RBNode):

        # In the same way
        left_ptr = high.left
        high.left = left_ptr.right
        left_ptr.right = high

        left_ptr.is_red = high.is_red
        high.is_red = True
        return left_ptr

    # Call this method when concurrent red nodes occur
    def flip(self, high: RBNode):
        # Set the highest node to be red
        high.is_red = True
        # Its childern to be black
        high.left.is_red = False
        high.right.is_red = False

    def fix_up(self, node: RBNode):
        # Fix right-leaning red note
        if self.check_red(node.right) and not self.check_red(node.left):
            node = self.rotate_left(node)

        # Fix two consecutive red notes
        if self.check_red(node.left) and self.check_red(node.left.left):
            node = self.rotate_right(node)

        # Fix two red children
        if self.check_red(node.left) and self.check_red(node.right):
            self.flip(node)

        return node

    # Call this method to insert one element
    def insert(self, val):

        # If no root, let it be root
        if self.root is None:
            # Black root
            self.root = RBNode(val)
            self.root.is_red = False
            return

        def insert_helper(node: RBNode, val):
            if node is None:
                return RBNode(val)

            if val < node.val:
                node.left = insert_helper(node.left, val)
            elif val > node.val:
                node.right = insert_helper(node.right, val)

            # Fix the tree
            return self.fix_up(node)

        self.root = insert_helper(self.root, val)
        self.root.is_red = False

    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def inOrder_helper(self, node: RBNode):
        if node is not None:
            self.inOrder_helper(node.left)
            print(node.val)
            self.inOrder_helper(node.right)

    def inOrder(self):
        self.inOrder_helper(self.root)


if __name__ == "__main__":
    tree = LLRBTree()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1232, 1234524, 231425123]
    for val in values:
        tree.insert(val)

    tree.inOrder()
