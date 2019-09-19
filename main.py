from lib import maze, mazeturtle, turtlebrain

image_maze = maze.Maze("mazes\\easy10x10.png")
turtle_boi = mazeturtle.MazeTurtle(image_maze.get_start(), image_maze)
turtle_brain = turtlebrain.TurtleBrain(turtle_boi)

turtle_brain.discover_maze()