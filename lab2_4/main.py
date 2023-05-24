# Sources:  https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
#           https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_binary_tree(array):
    if not array:
        return None

    # sort the array
    array = sorted(array)

    # find middle index
    root = Node(array[len(array) // 2])

    # make the middle element the root
    queue = deque([(root, 0, len(array) - 1)])

    while queue:
        # start and end is the range of values considered for the current node
        node, start, end = queue.popleft()
        mid = (start + end) // 2

        # the values are smaller than the middle element, so they are added to the left subtree
        if mid > start:
            node.left = Node(array[(start + mid - 1) // 2])
            queue.append((node.left, start, mid - 1))

        # the values are greater than the middle element, so they are added to the right subtree
        if mid < end:
            node.right = Node(array[(start + mid + 1) // 2])
            queue.append((node.right, mid + 1, end))

    return root


# inorder traversal - left, root, right
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)


# postorder traversal - left, right, root
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')


# preorder traversal - root, left, right
def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)


if __name__ == '__main__':
    elements = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    binary_tree = create_binary_tree(elements)
    print('Inorder traversal:')
    inorder_traversal(binary_tree)
    print('\nPreorder traversal:')
    preorder_traversal(binary_tree)
    print('\nPostorder traversal:')
    postorder_traversal(binary_tree)