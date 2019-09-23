from PIL import Image
from lib.constants import *

class Maze():
    def __init__(self, maze_base: str, entryPoint = None, exitPoint = None, wall_colour = MAZE.DEFAULT_WALL_COLOUR) -> None:
        super().__init__()
        self.maze_map = Image.open(maze_base).convert('RGB')

        self.wall_colour = wall_colour

        possibleEntryPoint, possibleExitPoint = self.find_holes()

        #todo: assign unassigned opening to entry/exit point
        if entryPoint is None:
            self.entryPoint = possibleEntryPoint

        if exitPoint is None:
            self.exitPoint = possibleExitPoint

    @property
    def width(self):
        return self.maze_map.width

    @property
    def height(self):
        return self.maze_map.height

    @property
    def size(self):
        return self.maze_map.size

    def get_start(self):
        return self.entryPoint

    def get_end(self):
        return self.exitPoint

    def check_position(self, xy) -> bool:
        if (0 <= xy[X] < self.width) and (0 <= xy[Y] < self.height):
            captured_colour = self.maze_map.getpixel(xy)[:3]
            if captured_colour == self.wall_colour:
                return MAZE.WALL
            else:
                return MAZE.PATH
        else:
            return MAZE.WALL

    def find_holes(self) -> list:
        holes = []
        #left side and right side
        for y in range(self.height):
            check_point = (0, y)
            if self.check_position(check_point) == MAZE.PATH:
                holes.append(check_point)

            check_point = (self.width - 1, y)
            if self.check_position(check_point) == MAZE.PATH:
                holes.append(check_point)

        if len(holes) >= 2:
            return holes[:2]
        for x in range(self.width):
            check_point = (x, 0)
            if self.check_position(check_point) == MAZE.PATH:
                holes.append(check_point)

            check_point = (x, self.height - 1)
            if self.check_position(check_point) == MAZE.PATH:
                holes.append(check_point)

        return holes[:2]



