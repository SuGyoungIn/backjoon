import sys
input = sys.stdin.readline
n = int(input())

tree = {}
for _ in range(n):
    p,l,r = map(str,input().split())
    tree[p] = [l,r]

def preOrder(node):
    if node != '.':
        print(node, end="")
        preOrder(tree[node][0])
        preOrder(tree[node][1])

def inOrder(node):
    if node != '.':
        inOrder(tree[node][0])
        print(node, end="")
        inOrder(tree[node][1])

def postOrder(node):
    if node != '.':
        postOrder(tree[node][0])
        postOrder(tree[node][1])
        print(node, end="")

preOrder('A')
print()
inOrder('A')
print()
postOrder("A")