import os, time
from lib import turtlebrain, maze, mazeturtle

mazes = os.listdir('mazes')
print(" "*14+"Maze"+" "*14 +"| Time")
for maze_path in mazes:
    start_time = time.time()
    usable_maze = maze.Maze('mazes\\'+maze_path)

    testing_turtle = mazeturtle.MazeTurtle(usable_maze.get_start(), usable_maze)
    testing_brain = turtlebrain.TurtleBrain(testing_turtle)

    testing_brain.discover_maze()
    testing_brain.solve_maze()

    print('%-31s | %.3fs'%(maze_path, time.time()-start_time))