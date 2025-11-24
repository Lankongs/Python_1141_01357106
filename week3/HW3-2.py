def build_height(preOrder, inOrder):
    if not preOrder or not inOrder:
        return 0
    root = preOrder[0]
    mid = inOrder.index(root)
    left_h = build_height(preOrder[1:1+mid], inOrder[:mid])
    right_h = build_height(preOrder[1+mid:], inOrder[mid+1:])
    return 1 + max(left_h, right_h)

preOrder = list(map(int, input().split()))
inOrder = list(map(int, input().split()))
print(build_height(preOrder, inOrder))