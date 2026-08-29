class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)

    def print_tree(self):
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, prefix, is_left):
        if node is None:
            return
        if node.right is not None:
            self._print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left is not None:
            self._print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    tree = BinaryTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        tree.insert(value)

    print("Visual:")
    tree.print_tree()

    print("\nPreorder:", tree.preorder())
    print("Inorder:", tree.inorder())
    print("Postorder:", tree.postorder())
