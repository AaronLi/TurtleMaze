class MazeGraph:
    def __init__(self):
        self.graph = {}
        self.distances = {}

    def add_connection(self, from_coord, to_coord):
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