li_pre = []
li_post = []
size = 0

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def preorder(node):
    li_pre.append(node.val)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    li_post.append(node.val)

def solution(li_node):
    global size
    size = len(li_node)
    for i in range(size):
        li_node[i].append(i+1)
    li_node.sort(key=lambda x:(-x[1],x[0]))

    root = 0
    for node in li_node:
        if not root:
            root = Tree(node[2])
        else:
            cur = root
            while True:
                if node[] < cur.x:
                    if cur.left:
                        cur = cur.left
                        continue
                    else:
                        cur.left = Tree(node)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                        continue
                    else:
                        cur.right = Tree(node)
                        break
                    break
    result = []
    preorder(root)
    postorder(root)
    result.append(li_pre)
    result.append(li_post)
    return result

print(solution(	[[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))