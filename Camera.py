from pygame import *
from constants import *

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    #apply camera to target
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

#camera that is centered on player sprite
def simple_camera(camera, target_rect):
    left, top, _, _ = target_rect
    _, _, width, height = camera
    return Rect(-left + HALF_WINDOW_WIDTH, -top + HALF_WINDOW_HEIGHT, width, height)

#camera that stops scrolling at edges of the level
def complex_camera(camera, target_rect):
    left, top, _, _ = target_rect
    _, _, width, height = camera
    left, top, _, _ = -left + HALF_WINDOW_WIDTH, -top + HALF_WINDOW_HEIGHT, width, height
    left = min(0, left)                                  # stop scrolling at the left edge
    left = max(-(camera.width - WINDOW_WIDTH), left)    # stop scrolling at the right edge
    top = max(-(camera.height - WINDOW_HEIGHT), top)    # stop scrolling at the bottom
    top = min(0, top)                                     # stop scrolling at the top
    return Rect(left, top, width, height)