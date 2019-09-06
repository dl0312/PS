import functools
import sys
sys.setrecursionlimit(10**6)

preorder_lst = []
postorder_lst = []

class Tree:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left = self.right = None


def preorder(node):
    preorder_lst.append(node.index)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    postorder_lst.append(node.index)


def compare(info1, info2):
    if info1[1] != info2[1]:
        return info2[1] - info1[1]
    else:
        return info1[0] - info2[0]


def solution(nodeinfo):
    answer = []
    nodeinfo_with_index = [info + [idx+1] for idx, info in enumerate(nodeinfo)]
    nodeinfo_with_index.sort(key=functools.cmp_to_key(compare))
    root_node = None
    for node in nodeinfo_with_index:
        if not root_node:
            root_node = Tree(node[0], node[1], node[2])
        else:
            x = node[0]
            curr_node = root_node
            while True:
                if x < curr_node.x:
                    if curr_node.left:
                        curr_node = curr_node.left
                        continue
                    else:
                        curr_node.left = Tree(node[0], node[1], node[2])
                        break
                if x > curr_node.x:
                    if curr_node.right:
                        curr_node = curr_node.right
                        continue
                    else:
                        curr_node.right = Tree(node[0], node[1], node[2])
                        break
                break
    preorder(root_node)
    postorder(root_node)
    answer.append(preorder_lst)
    answer.append(postorder_lst)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo)) # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

nodeinfo = 	[[8, 6], [10, 2]]
print(solution(nodeinfo)) # [[1, 2], [2, 1]]

nodeinfo = 	[[8, 6], [2, 2]]
print(solution(nodeinfo)) # [[1, 2], [2, 1]]