class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._addd(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    def _find(self, val, node):
        if val == node.val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)
    def deleteTree(self):
        self.root = None
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.v) + ' ')
            self._printTree(node.right)


