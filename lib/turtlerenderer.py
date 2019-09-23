from lib import mathtools
from lib.constants import *
import time, cv2
import numpy as np
from PIL import Image


class TurtleRenderer:
    #uses the maze map to set the size of the video that is outputted
    def __init__(self, maze_map, save_video = False, show_progress = False, frame_rate = 60) -> None:

        self.video_size = mathtools.list_mul(maze_map.size, (10, 10))
        self.save_video = save_video
        self.show_progress = show_progress
        self.frame_rate = frame_rate

        self.last_display_update = time.time()

        if self.save_video:
            self.video_recorder = cv2.VideoWriter("turtle_path.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 120,
                                                  self.video_size, True)

    def render_state(self, turtle_brain, paths=()):
        if not self.save_video and not self.show_progress:
            return
        base_frame = Image.new('RGB', turtle_brain.maze.size)

        for coordinate in turtle_brain.graph.graph:
            base_frame.putpixel(coordinate, COLOUR.WHITE)

        for open_point in turtle_brain.open_set:
            base_frame.putpixel(open_point, COLOUR.BLUE)

        for i, path in enumerate(paths):
            for coordinate in path:
                base_frame.putpixel(coordinate, VIDEO_RENDERING.PATH_COLOURS[i])

        base_frame.putpixel(turtle_brain.body.pos, COLOUR.TURTLE_GREEN)

        opencv_frame = np.array(base_frame)
        opencv_frame = cv2.cvtColor(opencv_frame, cv2.COLOR_BGR2RGB)
        opencv_frame = cv2.resize(opencv_frame, self.video_size, interpolation=cv2.INTER_AREA)

        if self.show_progress:
            cv2.imshow("Turtle Progress", opencv_frame)

            time_difference = (time.time() - self.last_display_update)*1000

            if self.frame_rate <= -1:
                wait_time = 1 # minimum delay
            elif self.frame_rate == 0:
                wait_time = 0 # use key to step program
            else:
                # calculate how long to wait to maintain proper framerate
                wait_time = int(max((1000 / self.frame_rate) - time_difference, 1))

            cv2.waitKey(wait_time)

            self.last_display_update = time.time()

        if self.save_video:
            self.video_recorder.write(opencv_frame)