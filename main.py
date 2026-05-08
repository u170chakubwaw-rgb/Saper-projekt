from tkinter import *
import settings
import utils
from cell import Cell
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



btn1 = Button (
    center_frame,# w srodku centre frame
    bg = 'blue',
    text='first Button'
)
# plansza
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_button_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y,
        )



center_frame.place(
    x=utils.width_prct(25),
    y=utils.heigth_prct(25))




#run the window
root.mainloop()

