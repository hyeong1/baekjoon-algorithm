def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])  # left c
        preorder(tree[root][1])  # right c


def inorder(root):
    if root != ".":
        inorder(tree[root][0])  # left
        print(root, end="")
        inorder(tree[root][1])  # right


def postorder(root):
    if root != ".":
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end="")


n = int(input())
tree = {}
for i in range(n):
    p, lc, rc = input().split()
    tree[p] = [lc, rc]

preorder("A")
print()
inorder("A")
print()
postorder("A")