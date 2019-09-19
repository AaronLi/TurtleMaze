from lib.constants import *
from PIL import Image


class MazeGraph:
    def __init__(self):
        self.graph = {}
        self.distances = {}
        self.max_x = None
        self.max_y = None
        self.min_x = None
        self.min_y = None

    def add_connection(self, from_coord, to_coord):
        if self.max_x is None:
            self.max_x = max(from_coord[X], to_coord[X])
        else:
            self.max_x = max(from_coord[X], to_coord[X], self.max_x)

        if self.max_y is None:
            self.max_y = max(from_coord[Y], to_coord[Y])
        else:
            self.max_y = max(from_coord[Y], to_coord[Y], self.max_y)

        if self.min_x is None:
            self.min_x = min(from_coord[X], to_coord[X])
        else:
            self.min_x = min(from_coord[X], to_coord[X], self.min_x)

        if self.min_y is None:
            self.min_y = min(from_coord[Y], to_coord[Y])
        else:
            self.min_y = min(from_coord[Y], to_coord[Y], self.min_y)

        if from_coord in self.graph:
            self.graph[from_coord].add(to_coord)
        else:
            self.graph[from_coord] = {to_coord}

    def __add__(self, other):
        if type(other) != MazeGraph:
            raise TypeError("Must be adding two MazeGraphs")

        for point in other:
            for destination in list(other.graph[point]):
                self.add_connection(point, destination)

        return self

    def get_neighbours(self, pos):
        return self.graph.get(pos)

    def get_distance(self, p1, p2):
        return 1

    def render_graph(self):
        graph_width = self.max_x - self.min_x + 1
        graph_height = self.max_y - self.min_y + 1
        image_dimensions = (graph_width, graph_height)

        draw_image = Image.new('1', image_dimensions)
        for coordinate in self.graph:
            draw_position = (coordinate[X] - self.min_x, coordinate[Y] - self.min_y)
            draw_image.putpixel(draw_position, 1)

        draw_image.save('graph_rendering.png')
