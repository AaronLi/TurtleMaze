from lib import maze, mazeturtle, turtlebrain, turtlerenderer
import time

image_maze = maze.Maze("mazes\\02 hard50x50.png")
turtle_boi = mazeturtle.MazeTurtle(image_maze)
turtle_renderer = turtlerenderer.TurtleRenderer(image_maze, save_video=False, show_progress=True, frame_rate=-1)
turtle_brain = turtlebrain.TurtleBrain(turtle_boi, turtle_renderer)

discover_maze_start = time.time()
turtle_brain.discover_maze()
print("Maze discovery finished in %.3f seconds" % (time.time() - discover_maze_start))

turtle_brain.graph.render_graph()

traverse_and_solve_maze_start = time.time()
turtle_brain.solve_maze()
print("Maze solved and traversed in %.3f seconds" % (time.time() - traverse_and_solve_maze_start))

print('total time %.3f seconds' % (time.time() - discover_maze_start))
