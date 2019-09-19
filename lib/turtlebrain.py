from lib import mazeturtle, maze, mazegraph, mathtools
import heapq
from lib.constants import *

class TurtleBrain():
    def __init__(self, body :mazeturtle.MazeTurtle):
        self.graph = mazegraph.MazeGraph()
        self.body = body
        self.closed_set = set()
        self.open_set = set()

    def face_cardinal(self, direction):
        while direction - self.body.facing != 0:
            if direction - self.body.facing < 0:
                self.body.turn_left()
            else:
                self.body.turn_right()

    def solve_maze(self):
        self.goto(self.body.maze.get_start())
        path_to_end = self.pathfind_to(self.body.maze.get_end())
        self.render_path(path_to_end)
        self.follow_path(path_to_end)

    def goto(self, pos):
        path = self.pathfind_to(pos)
        self.follow_path(path)

    def rotate_for_move(self, desired_move_directions):
        desired_move_directions = tuple(desired_move_directions)

        #TODO: scale desired move down to unit vector

        if desired_move_directions == CARDINAL.NORTH_MOVE:
            self.face_cardinal(CARDINAL.NORTH)
        elif desired_move_directions == CARDINAL.EAST_MOVE:
            self.face_cardinal(CARDINAL.EAST)
        elif desired_move_directions == CARDINAL.SOUTH_MOVE:
            self.face_cardinal(CARDINAL.SOUTH)
        elif desired_move_directions == CARDINAL.WEST_MOVE:
            self.face_cardinal(CARDINAL.WEST)

    def discover_maze(self):
        self.check_directions()

        while len(self.open_set) > 0:
            new_target = self.open_set.pop()
            #print("moving from", self.body.pos, "to", new_target)

            path = self.pathfind_to(new_target)
            self.follow_path(path)
            self.check_directions()

    def follow_path(self, path):
        while len(path) > 0:
            next_node = path.pop(0)

            position_difference = mathtools.list_sub(next_node, self.body.pos)

            if position_difference == (0,0):
                continue
            self.rotate_for_move(position_difference)
            self.body.move_forward()

    def check_directions(self):
        for i in range(4):
            check_result = self.body.check_front()
            if check_result is not None:
                if check_result not in self.closed_set:
                    self.open_set.add(check_result)
                self.graph.add_connection(self.body.pos, check_result)
                self.closed_set.add(check_result)
            self.body.turn_right()

    def pathfind_to(self, destination):
        start_point = self.body.pos

        gScore = {}
        gScore[start_point] = 0

        fScore = {}
        fScore[start_point] = mathtools.euclidean(start_point, start_point)
        cameFrom = {}
        closedset = set()

        openSet = [(fScore[start_point], start_point)]

        heapq.heapify(openSet)

        while len(openSet) > 0:
            current = heapq.heappop(openSet)

            if current[1] == destination:
                return self.__reconstruct_path(cameFrom, current[1])

            closedset.add(current[1])
            neighbours = self.graph.get_neighbours(current[1])
            if neighbours is None:
                continue
            for neighbour in neighbours:
                if neighbour in closedset:
                    continue
                tentative_gscore = gScore[current[1]] + self.graph.get_distance(current[1], neighbour)
                if neighbour not in gScore:
                    gScore[neighbour] = INFINITY
                if tentative_gscore < gScore[neighbour]:
                    cameFrom[neighbour] = current[1]
                    gScore[neighbour] = tentative_gscore
                    fScore[neighbour] = gScore[neighbour] + mathtools.euclidean(start_point, neighbour)
                    new_open_node = (fScore[neighbour], neighbour)
                    if new_open_node not in openSet:
                        heapq.heappush(openSet, new_open_node)
        return None

    def __reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

    def render_path(self, path):
        draw_image = self.body.maze.maze_map.copy()

        for coordinate in path:
            draw_image.putpixel(coordinate, (255,0,0))

        draw_image.save("path_rendering.png")