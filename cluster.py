from point import Point
from statistics import median


class Cluster:
    def __init__(self, cluster_id, initial_point):
        self.id = cluster_id
        self._centroid = Point(str(cluster_id) + '_center')
        #  IMPORTANT NOTE: data type of _points changed from dict to list because of name issues
        self._points = [initial_point]  # List of Point object
        self.compute_centroid()

    def compute_centroid(self):
        """
        Function to recompute new centroid of current points
        :return: Boolean value showing if centroid changed
        """
        if not self._points:
            print("Can't compute center without points")
            return

        # Saving old state
        old_centroid = tuple(self._centroid.coordinates)

        # Now go through each point and set the coordinates by the l1norm for median point
        some_point: Point = self._points[0]
        number_of_coordinates = len(some_point.coordinates)
        new_coordinates: list = [0] * number_of_coordinates

        # Now go through each point and set the coordinates by the l1norm for median point
        if len(self._points) == 1:
            self._centroid.set_coordinates(some_point.coordinates)
            return False
        for coordinate_index in range(number_of_coordinates):
            sorted_points = sorted(self._points, key=lambda point: point.coordinates[coordinate_index])
            sorted_list: list = [point.coordinates[coordinate_index] for point in sorted_points]
            value = median(sorted_list)
            new_coordinates[coordinate_index] = value

        self._centroid.set_coordinates(new_coordinates)
        is_changed = (old_centroid != tuple(self._centroid.coordinates))
        return is_changed

    def add_point(self, point):
        """
        Add point to the cluster
        :param point: Point to add
        """
        self._points.append(point)

    def remove_point(self, point=None):
        """
        Remove given point from the cluster. If point isn't provided then cluster is cleared.
        :param point: Point to remove or nothing
        """
        if not point:
            self._points = []
        elif point not in self._points:
            print('Point with name {} does not belong to cluster {}'.format(point.name, self.id))
        else:
            self._points.remove(point)

    def print(self):
        print('############################################')
        print('Cluster:', self.id)
        print('Number of points:', len(self._points))
        print('Centroid:', self._centroid.coordinates)
        print('Points:', ' '.join(sorted([x.name for x in self._points])))

    def compute_loss(self):
        distances = [self._centroid.distance_to(point.coordinates) for point in self._points]
        return sum(distances)

    def compute_SSE(self):
        errors = [self._centroid.distance_to(point.coordinates)**2 for point in self._points]
        return sum(errors)

    @property
    def centroid(self):
        return self._centroid.coordinates

    @property
    def number_of_points(self):
        return len(self._points)
