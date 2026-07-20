from CodeExamples.binary_search_tree import BinarySearchTree
from CodeExamples.tree_node import TreeNode

# Algorithm: Inorder Traversal (Left → Root → Right)
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)

# Algorithm: Preorder Traversal (Root → Left → Right)
def preorder(node):
    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)

# Algorithm: Postorder Traversal (Left → Right → Root)
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data)

def main():
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)

    print("Inorder traversal:")
    inorder(bst.root)
    print()

    print("Preorder traversal:")
    preorder(bst.root)
    print()

    print("Postorder traversal:")
    postorder(bst.root)

if __name__ == "__main__":
    main()
