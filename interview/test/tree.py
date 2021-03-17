class Tree:
    MAX_CHILD_NUM = 2

    class TreeNode:
        def __init__(self, parent):
            self.parent = parent
            self.child = [-1] * Tree.MAX_CHILD_NUM

    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.treenode = [0] * (nodeNum + 1)

        for i in range(1, nodeNum + 1):
            self.treenode[i] = self.TreeNode(-1)

    def addChild(self, parent, child):
        found = -1

        for i in range(0, self.MAX_CHILD_NUM):
            if self.treenode[parent].child[i] == -1:
                found = i
                break

        if found == -1:
            return

        self.treenode[parent].child[found] = child
        self.treenode[child].parent = parent

    def getRoot(self):
        for i in range(1, self.nodeNum):
            if self.treenode[i].parent == -1:
                return i

        return -1

    def preOrder(self, root):

        print(root, end=' ')

        for i in range(0, self.MAX_CHILD_NUM):
            child = self.treenode[root].child[i]
            if child != -1:
                self.preOrder(child)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        node, edge = map(int, input().split())

        tree = Tree(node)

        numbers = [int(num) for num in input().split()]

        for i in range(0, edge * 2, 2):
            parent = numbers[i]
            child = numbers[i + 1]
            tree.addChild(parent, child)

        root = tree.getRoot()
        print("#%d" % test_case, end=' ')
        tree.preOrder(root)
        print()


if __name__ == "__main__":
    main()