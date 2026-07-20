from CodeExamples.tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)

        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    # Search for a value
    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        if value < node.data:
            return self._contains(node.left, value)

        return self._contains(node.right, value)

    # Find the minimum value
    def find_min(self):
        current = self.root

        while current.left:
            current = current.left

        return current.data

    # Find the maximum value
    def find_max(self):
        current = self.root

        while current.right:
            current = current.right

        return current.data


def main():
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)
        print(value)

    print()
    
    print(bst.contains(40))
    print(bst.contains(90))

    print()

    print("Minimum:", bst.find_min())
    print("Maximum:", bst.find_max())

if __name__ == "__main__":
    main()