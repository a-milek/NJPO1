# Implement a k-d tree
# Pseudocode source: https://www.baeldung.com/cs/k-d-trees
# Other sources: https://en.wikipedia.org/wiki/K-d_tree

from operator import itemgetter


def kdtree(list_of_points, depth=0):
    if not points:
        return None

    # Select axis based on depth so that axis cycles through all valid values
    k = len(list_of_points[0])  # number of dimensions of a point eg. (x, y, z) = 3
    axis = depth % k

    # Sort point list and choose median as pivot element
    # retrieve the axis value from the point and sort by it
    list_of_points.sort(key=itemgetter(axis))
    median_index = len(list_of_points) // 2
    median = list_of_points[median_index]

    # Create node and construct subtrees recursively
    node = {
        #  let location := median;
        "location": median,
        #  let leftChild := kdtree(points in list before median, depth+1);
        "leftChild": kdtree(list_of_points[:median_index], depth + 1),
        #  let rightChild := kdtree(points in list after median, depth+1);
        "rightChild": kdtree(list_of_points[median_index + 1:], depth + 1)
    }

    return node


# main
if __name__ == '__main__':
    points = [(1, 0), (2, 40), (15, 16), (51, 12), (8, 1), (23, 5), (32, 12), (3, 9), (1, 5), (8, 3), (3, 20), (4, 12), (12, 5)]
    tree = kdtree(points)
    print(tree)

    points = [(4, 3, 5), (2, 1, 3), (5, 4, 2), (9, 6, 7), (4, 7, 8), (8, 1, 9), (7, 2, 1), (6, 3, 4), (3, 9, 6)]
    tree = kdtree(points)
    print(tree)

    points = [(1, 3, 5, 8), (2, 1, 3, 4), (5, 4, 2, 1), (9, 6, 7, 2), (4, 7, 8, 3), (8, 1, 9, 4), (7, 2, 1, 5), (6, 3, 4, 6), (3, 9, 6, 7)]
    tree = kdtree(points)
    print(tree)
