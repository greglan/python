import matplotlib.pyplot as plt
from random import randint


def min_point(points, n_points):
    """
    Return the index of the closest point to (0,0)
    :param points: tuple of list for each coordinate
    :param n_points: number of points
    :return: the index of the selected point in the list
    """
    min_y_indexes = [0]
    min_y = points[1][0]

    # Find minimum y
    for k in range(1, n_points):
        if points[1][k] < min_y:
            min_y_indexes = [k]
        elif points[1][k] == min_y:
            min_y_indexes.append(k)

    # Among the points having the smallest y, find the points having the smallest x
    min_x = points[0][min_y_indexes[0]]
    min_index = min_y_indexes[0]

    for k in min_y_indexes:
        if points[0][k] < min_x:
            min_index = k

    return min_index


def orient(points, i, j, k):  # FIXME: add doc
    """

    :param points:
    :param i:
    :param j:
    :param k:
    :return:
    """
    a = points[0][j] - points[0][i]
    b = points[1][j] - points[1][i]
    c = points[0][k] - points[0][i]
    d = points[1][k] - points[1][i]

    # Determinant
    r = 0.5 * (a * d - b * c)

    if r == 0:
        return 0
    elif r > 0:
        return 1
    else:
        return -1


def get_next_point(points, n_points, current_point):
    """
    Returns the next point in the convex hull
    :param points: tuple of list
    :param n_points: number of points
    :param current_point: current point
    :return: the index of the next point
    """
    if current_point == 0:
        next_point_index = 1
    else:
        next_point_index = 0

    for point in range(n_points):
        if point != current_point and orient(points, current_point, point, next_point_index) > 0:
            next_point_index = point

    return next_point_index


def jarvis_march(points):
    """
    Returns the convex hull of the given set of point

    :param points:
    :return: ordered list of the indexes of the point
    """
    n_points = len(points[0])
    convex_hull_indexes = [min_point(points, n_points)]
    next_point = get_next_point(points, n_points, convex_hull_indexes[0])

    while next_point != convex_hull_indexes[0]:
        convex_hull_indexes.append(next_point)
        next_point = get_next_point(points, n_points, convex_hull_indexes[-1])

    # Convert the convex hull to coordinates
    convex_hull_x = []
    convex_hull_y = []

    for point in convex_hull_indexes:
        convex_hull_x.append(points[0][point])
        convex_hull_y.append(points[1][point])

    return convex_hull_x, convex_hull_y


def show_points(x, y):
    plt.scatter(x, y)


def random_points(n: int, x, y):
    """
    Returns the coordinates of a set of random points. No doublon is allowed.
    :type n: int
    :param n: number of points
    :param x: x range
    :param y: y range
    :return: a tuple of list
    """
    X = []
    Y = []
    generated_points = []
    i = 0

    while i < n:
        u = randint(-x, x)
        v = randint(-y, y)

        # If new point doesn't exist already
        if generated_points.count([u, v]) == 0:
            generated_points.append([u, v])
            X.append(u)
            Y.append(v)
            i += 1

    return X, Y


N_POINTS = 6
RANGE = 10

points = random_points(N_POINTS, RANGE, RANGE)
show_points(points[0], points[1])

convex_hull_x, convex_hull_y = jarvis_march(points)
n = len(convex_hull_x)

# Plot the convex hull
for i in range(n - 1):
    plt.plot([convex_hull_x[i], convex_hull_x[i + 1]], [convex_hull_y[i], convex_hull_y[i + 1]], linestyle='dashed')
plt.plot([convex_hull_x[-1], convex_hull_x[0]], [convex_hull_y[-1], convex_hull_y[0]], linestyle='dashed')
plt.show()
