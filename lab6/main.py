from operator import itemgetter


class KDTree:
    def __init__(self, points=None, depth=0):
        self.root = None
        self.count = 0
        self.dimensions = 0

        if points is not None:
            self.dimensions = len(points[0])
            self.root = self._build(points, depth)

    def __len__(self):
        return self._height(self.root)

    def __iter__(self):
        yield from self._traverse(self.root)

    def __contains__(self, point):
        return self.search(self.root, point, 0)

    def __getitem__(self, point):
        return self.search(self.root, point, 0)

    def __setitem__(self, point):
        self.root = self._insert(self.root, point, 0)

    def __lshift__(self, point):
        self.root = self._insert(self.root, point, 0)

    def __pow__(self, exponent):
        self._fill_with_random_values(self.root, exponent)
        while self._count(self.root) != self.count ** exponent:
            self._fill_with_random_values(self.root, exponent)

    def __str__(self):
        return self._draw_tree(self.root)

    def _build(self, points, depth):
        if not points:
            return None

        axis = depth % self.dimensions
        points.sort(key=itemgetter(axis))
        median_index = len(points) // 2
        median = points[median_index]

        node = {
            "location": median,
            "left_child": self._build(points[:median_index], depth + 1),
            "right_child": self._build(points[median_index + 1:], depth + 1)
        }

        self.count += 1
        return node

    def _traverse(self, node):
        if node is not None:
            yield node["location"]
            yield from self._traverse(node["left_child"])
            yield from self._traverse(node["right_child"])

    def search(self, node, point, depth):
        if node is None:
            return False

        if node["location"] == point:
            return True

        current_depth = depth % self.dimensions

        if point[current_depth] < node["location"][current_depth]:
            return self.search(node["left_child"], point, depth + 1)
        else:
            return self.search(node["right_child"], point, depth + 1)

    def _insert(self, node, point, depth):
        if node is None:
            return {"location": point, "left_child": None, "right_child": None}

        axis = depth % self.dimensions

        if point[axis] < node["location"][axis]:
            node["left_child"] = self._insert(node["left_child"], point, depth + 1)
        else:
            node["right_child"] = self._insert(node["right_child"], point, depth + 1)

        return node

    def _height(self, node):
        if node is None:
            return 0

        return max(self._height(node["left_child"]), self._height(node["right_child"])) + 1

    def _count(self, node):
        if node is None:
            return 0

        return 1 + self._count(node["left_child"]) + self._count(node["right_child"])

    def _fill_with_random_values(self, node, exponent):
        if node is None:
            return


# main
if __name__ == '__main__':
    points = [[1, 0], [2, 40], [15, 16], [51, 12], [8, 1], [23, 5], [32, 12], [3, 9], [1, 5], [8, 3], [3, 20], [4, 12],
              [12, 5]]
    tree = KDTree(points)
    points = [[4, 3, 5], [2, 1, 3], [5, 4, 2], [9, 6, 7], [4, 7, 8], [8, 1, 9], [7, 2, 1], [6, 3, 4], [3, 9, 6]]
    tree = KDTree(points)
    assert (3, 9, 6) in tree

    points = [[1, 3, 5, 8], [2, 1, 3, 4], [5, 4, 2, 1], [9, 6, 7, 2], [4, 7, 8, 3], [8, 1, 9, 4], [7, 2, 1, 5],
              [6, 3, 4, 6], [3, 9, 6, 7]]
    tree = KDTree(points)
    assert [3, 9, 6, 7] in tree

    print("All assertions passed!")
