from lib import maze, mazeturtle, turtlebrain
import time
image_maze = maze.Maze("mazes\\medium20x20.png")
turtle_boi = mazeturtle.MazeTurtle(image_maze.get_start(), image_maze)
turtle_brain = turtlebrain.TurtleBrain(turtle_boi, save_video=True)

discover_maze_start = time.time()
turtle_brain.discover_maze()
print("Maze discovery finished in %.3f seconds"%( time.time() - discover_maze_start))

turtle_brain.graph.render_graph()

traverse_and_solve_maze_start = time.time()
turtle_brain.solve_maze()
print("Maze solved and traversed in %.3f seconds"%(time.time() - traverse_and_solve_maze_start))

print('total time %.3f seconds'%(time.time() - discover_maze_start))