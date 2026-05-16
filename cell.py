from tkinter import Button
from tkinter import Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y



        #append object to Cell.all.list
        Cell.all.append(self)
    def create_button_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )

        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn



    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text=f'Cell left:{settings.CELL_COUNT}',
            font=('Comic Sans', 34),
        )
        Cell.cell_count_label_object = lbl




    def left_click_actions(self, event):
        if self.is_mine_candidate or self.is_opened:
            return
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length() == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            #jesli mines count bedzie rowny cells left count, gracz wygrywa
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Wygrałeś grę', 'Gratulację', 0)




    def get_cell_by_axis(self, x,y):
        #return a cell object based on x,y values
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                    return cell




    @property #read only
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]


        cells = [cell for cell in cells if cell is not None]
        return cells



    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length())
            #podmieniony tekst uzywajac zmiennej Cell.cell_count a nie stałej z settings
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells left: {Cell.cell_count}"
                )
            #jesli to by bylo mine_candidate to dla bezpiecznosci zmienmy kolor na systemButtoFace

        self.cell_btn_object.configure(bg='SystemButtonFace')

        self.is_opened = True

    def show_mine(self):
        #wyswietl informacje że gracz przegrał gre
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'Kliknąłeś na minę', 'PRZEGRAŁEŚ',0)
        sys.exit()



#prway przycisk klikniecie robi flage
    def right_click_actions(self, event):
        if self.is_opened:
            return

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
            )
            self.is_mine_candidate = True

        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace',
            )
            self.is_mine_candidate = False



    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )

        for picked_cell in picked_cells: # nie widzimy w terminalu jakie celle min zostaly randomowo wybrane
            picked_cell.is_mine = True




    def __repr__(self):
        return f"Cell({self.x},{self.y})"#cell numbers way more friendly napisane