from complex_function import *
from holomorphic_dynamics import HolomorphicDynamics

from tkinter import *
from PIL import Image, ImageTk
import numpy as np

frame_size = (1000, 1000)

window = Tk()

window.title('Mandelbrot set')

hd = HolomorphicDynamics(HiddinMandel, frame_size)
distances = (-1.5, -1.5, 2, 2)
frac = hd.color_points(distances)

frac = Image.fromarray(np.uint8(frac), 'RGB')
frac.save('output.jpg')
img = ImageTk.PhotoImage(image=frac)



canvas = Canvas(window,width=frame_size[1],height=frame_size[0])
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=img)

window.mainloop()