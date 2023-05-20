import numpy as np
from complex_function import *

class HolomorphicDynamics:

    def __init__(self, func: ComplexFunction, frame_size: tuple[int]) -> None:
        self.func = func
        self.frame_size = frame_size
    

    def color_points(self, window: tuple[float]) -> np.array:
        '''
        Color every pixel in `self.frame_size` based on `window` values applied on `self.func`, if that function converges

        `window`: x, y, w, h vaules that are shown on the window with `self.frame_size` pixels

        return: a matrix of `self.frame_size` shape filled with values based on `self.func` convergion
        '''


        x, y, w, h = window
        x_values = np.linspace(x, 
                               x + w, 
                               self.frame_size[1])

        y_values = np.linspace(y,
                               y + h,
                               self.frame_size[0])
        
        pixels = np.zeros((*self.frame_size, 3))
        for x_idx, real in enumerate(x_values):
            for y_idx, imag in enumerate(y_values):

                c = complex(real, imag)
                func = self.func(c)
                pixels[y_idx, x_idx] = func.converges()


        return pixels