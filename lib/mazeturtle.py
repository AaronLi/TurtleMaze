from lib.constants import *
from lib.maze import Maze
from operator import add

class MazeTurtle:
    def __init__(self, start_position, maze_in: Maze) -> None:
        self.pos = start_position
        self.facing = CARDINAL.NORTH
        self.maze = maze_in
        print("I'm a turtle starting at position", self.pos)

    def turn_right(self):
        self.facing = (self.facing + 1) % 4

    def turn_left(self):
        self.facing = (self.facing + 3) % 4

    def move_forward(self) -> bool:
        new_position = self.check_front()

        if new_position is not None:
            self.pos = new_position
            return True
        else:
            return False

    '''
    :return the position in front of the turtle if there is no wall, None if there is a wall
    '''
    def check_front(self):
        position_delta = CARDINAL.MOVE_COORDINATE_CHANGES[self.facing]
        front_space = tuple(map(add, self.pos, position_delta))
        if self.maze.check_position(front_space) == MAZE.PATH:
            return tuple(front_space)
        else:
            return None