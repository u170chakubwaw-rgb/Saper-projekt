from tkinter import *
import settings
import utils
from utils import heigth_prct

root =  Tk()
root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')
root.configure(bg="black")
root.resizable(False, False)
root.title("Saper")

top_frame = Frame(root,
                  bg="black", #change later to black
                  width=settings.WIDTH,
                  height=heigth_prct(25))
top_frame.place(x=0 ,y=0)

left_frame = Frame(root,
                   bg="black", #change later to black
                   width=utils.width_prct(25),
                   height = utils.heigth_prct(75),

                   )

left_frame.place(x=0 ,y=utils.heigth_prct(25))

center_frame = Frame(root,
                     bg='black', #change later to black
                     width=utils.width_prct(75),
                     height = utils.heigth_prct(75)
                     )
center_frame.place(
    x=utils.width_prct(25),
    y=utils.heigth_prct(25))
#run the window
root.mainloop()

