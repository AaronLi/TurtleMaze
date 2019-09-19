from lib import maze, mazeturtle, turtlebrain

image_maze = maze.Maze("mazes\\medium20x20.png")
turtle_boi = mazeturtle.MazeTurtle(image_maze.get_start(), image_maze)
turtle_brain = turtlebrain.TurtleBrain(turtle_boi)

turtle_brain.discover_maze()

turtle_brain.graph.render_graph()
turtle_brain.solve_maze()
turtle_brain.video_recorder.release()
