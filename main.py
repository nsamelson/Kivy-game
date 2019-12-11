from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,NumericProperty, ListProperty)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import random
import json
import os
from random import choice, randrange

Alpha =["A","B","C","D","E","F","G","H","I","J"]
Wreck=[]
Copy=[]
Sunk=[]
Sunkships =[]
Bingo = []
Ships=[]
ScoTab =[]
Max = []

filename = "result.json"
if (os.path.isfile(filename)):
    # lecture des scores

    with open(filename, "r") as file:
        data = json.load(file)
else:
    data = []

class WindowManager (ScreenManager):
    pass
class FirstWindow (Screen):
    pass
class SecondWindow (Screen):
    pass
class ThirdWindow (Screen):
    def on_enter(self, *args):

        print(Ships)

class FourthWindow (Screen):
    def on_pre_enter(self):
        Window.size = (1150, 500)
    def on_pre_leave(self):
        Window.size = (800, 600)
class FifthWindow (Screen,GridLayout):
    def on_enter(self):
        global ScoTab

class Counter(GridLayout):
    pass


class MyWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

    box = ObjectProperty(None)

    def on_box(self, *args):            #Grille
        for k in range(11):
            self.box.add_widget(Label(text=str(k)))
        for j in range(10):
            self.box.add_widget(Label(text=Alpha[j]))
            for i in range(10):
                self.box.add_widget(ImageButton(id=str(Alpha[j])+str(i+1)))

    def reset_board(self):
        image_buttons = [widget for widget in self.box.walk() if isinstance(widget, ImageButton)]
        for image_button in image_buttons:
            image_button.reset()

class ImageButton(ButtonBehavior,Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'blue.png'

    def reset(self):
        self.source = 'blue.png'
        self.disabled = False

    def on_press(self):
        global Ships
        self.source = "blue2.png"
        self.disabled = True
        print(self.id)
        for ship in Ships:
            for xy in ship:
                if self.id == xy:
                    self.source = "red.png"
                    ord = ship.index(xy)
                    ship.pop(ord)
                    Wreck.append(xy)
                    Bingo.append(xy)
                if len(ship) == 0:
                    Copy = Wreck.copy()
                    Sunk.append(Copy)
                    if len(Copy) ==2:
                        Sunkships.append("Torpedo")
                    elif len(Copy) ==3:
                        Sunkships.append("Submarine")
                    elif len(Copy) ==4:
                        Sunkships.append("Cruiser")
                    elif len(Copy) ==5:
                        Sunkships.append("Carrier")
                    Wreck.clear()
                    sunk = Ships.index(ship)
                    Ships.pop(sunk)


    def on_release(self):
        global Ships
        if len(Ships) ==0:
            Sunkships.clear()
            Sunkships.append("Touché Coulé")
            print("Touché coulé")
            self.popopen()
            Wreck.clear()
            Copy.clear()
            Sunk.clear()
            Sunkships.clear()
            Bingo.clear()
    def popopen(self):
        popsave = Pop()
        popsave.open()

class Pop (Popup):
    pass

class ScoreTab(GridLayout):
    global ScoTab
    tab = ObjectProperty(None)
    def on_tab(self, *args):
        for score in data:
            ScoTab.insert(0, score["score"])
            ScoTab.insert(0, score["player"])
        if len(ScoTab) < 16:
            for m in range(len(ScoTab)):
                self.tab.add_widget(Label(text=str(ScoTab[m])))
        else:
            for m in range(16):
                self.tab.add_widget(Label(text=str(ScoTab[m])))
        print(ScoTab)

class BestScore(GridLayout):
    global Max
    best = ObjectProperty(None)
    def on_best(self, *args):
        Max = data[0]
        for points in data:
            if points["score"] > Max["score"]:
                Max = points
        print(Max, "from here")
        self.best.add_widget(Label(text= Max["player"]))
        self.best.add_widget(Label(text= Max["score"]))
        print("Max :", Max)


def _collision(b, orientation, p_row, p_col, length):  # placing a ship on an existing ship is a collision
    sc = ['p', 's', 'c', 't']
    if orientation == 'horizontal':
        for i in range(-1, length + 1):  # add on space in front and one space after a ship
            if (b[p_row][p_col + i] in sc) or (b[p_row + 1][p_col + i] in sc) or (b[p_row - 1][p_col + i] in sc):
                return True  # add a space above and below
    else:  # orientation == 'vertical'
        for i in range(-1, length + 1):
            if b[p_row + i][p_col] in sc or b[p_row + i][p_col + 1] in sc or b[p_row + i][p_col - 1] in sc:
                return True  # add space to the left and right
    return False


def generate_game_board():
    length = {'p': 5, 's': 3, 'c': 4, 't': 2}
    top_bottom = ['*'] * 12  # Top or bottom frame
    mid = ['*'] + [' '] * 10 + ['*']  # The play area, create a list of lists to place ships
    board = [top_bottom, mid.copy(), mid.copy(), mid.copy(), mid.copy(), mid.copy(),  # make copies for play area
             mid.copy(), mid.copy(), mid.copy(), mid.copy(), mid.copy(), top_bottom]
    ships = ['p', 's', 's', 'c', 't']

    for ship in ships:
        orientation = choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            row = randrange(1, 11)
            col = randrange(1, 12 - length[ship])  # ensures ship will fit
            while _collision(board, orientation, row, col, length[ship]):  # if overlap, pick a new spot
                row = randrange(1, 11)
                col = randrange(1, 12 - length[ship])  # ensures ship will fit
            for i in range(length[ship]):
                board[row][col + i] = ship
        else:  # orientation == vertical
            row = randrange(1, 12 - length[ship])  # ensures ship will fit
            col = randrange(1, 11)
            while _collision(board, orientation, row, col, length[ship]):  # if overlap, pick a new spot
                row = randrange(1, 12 - length[ship])  # ensures ship will fit
                col = randrange(1, 11)
            for i in range(length[ship]):
                board[row + i][col] = ship

    bl = []  # convert board from a list of lists to a list of strings to match the file format
    for b in board:
        bl += [''.join(b)]
    return bl

grille = choice(["Grille_2.txt", "Grille_1.txt"])
def load_game_file():  # Implement as you need to load game files.
    with open(grille, 'r') as f:
        print(grille)
        board = f.readlines()
    return board
def subs_key(pos):
    return ord(pos[0]) * 100 + int(pos[1:])
def separate_subs(two_subs):  # find the 2 subs in the list
    # find the lowest value for a sub search across then down.

    sorted_subs = sorted(two_subs, key=subs_key)
    f = sorted_subs[0]
    # if there are 3 s across and not 3 down then horizontal else vertical
    if f[0] + str(int(f[1:]) + 1) in two_subs and f[0] + str(int(f[1:]) + 2) in two_subs and \
       not (str(chr(ord(f[0]) + 1)) + f[1:] in two_subs and str(chr(ord(f[0]) + 2)) + f[1:]) in two_subs:
        # horizontal sub
        sub_1 = [f, f[0] + str(int(f[1:]) + 1), f[0] + str(int(f[1:]) + 2)]
    else:
        # vertical sub
        sub_1 = [f, str(chr(ord(f[0]) + 1)) + f[1:], str(chr(ord(f[0]) + 2)) + f[1:]]
    # remove sub_1 from two_subs to get sub_2
    for pos in sub_1:
        two_subs.remove(pos)
    sub_2 = two_subs
    return sub_1, sub_2

def get_ships(random=True):
    locations = {'c': [], 'p': [], 's': [], 't': []}
    rows = ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '*']

    if not random:
        board = load_game_file()
        for row in board:  # print board
            print(row, end='')
    else:
        board = generate_game_board()
        for row in board:  # print board
            print(row)

    for row in range(1, 11):  # ignore first and last rows in board
        for i, c in enumerate(board[row]):
            if c in ['c', 'p', 's', 't']:
                locations[c] += [rows[row] + str(i)]  # Need to split of the 2 subs
    s1, s2 = separate_subs(locations['s'])  # the two subs end up on one list, find and put on separate lists
    del locations['s']  # remove the subs from the locations list
    return [v for k, v in locations.items()] + [s1] + [s2]  # add the 2 subs to the rest of the locations




class MyMainApp (App):
    moves = StringProperty('0')
    score = StringProperty('0')
    sink = StringProperty('ships touched')
    bingo = StringProperty("0")
    player_name = StringProperty("")


    def counter(self):
        self.sink = str("\n".join(Sunkships))   #It's for telling which ship has been sunk. I have also an issue with it where I must click another button to activate it and show the ship that sank
        self.moves = (str(int(self.moves) + 1))
        self.bingo = str(len(Bingo)+1)
        self.score = str("%.2f"% (100*int(self.bingo) / int(self.moves)))

    def btnsolo(self):
        print("solo")
    def btnduel(self):
        print("duel")

    def savescore(self):
        global data
        #global Max
        jsonresult = {'player': self.player_name, 'score': self.score}
        print(jsonresult)

        # ajout d'un nouveau score
        if self.player_name != "" or self.score != "0":
            data.append({'player': self.player_name, 'score': self.score})
        with open(filename, "w") as file:
            json.dump(data, file)
        """Max = data[0]
        for points in data:
            if points["score"] > Max["score"]:
                Max = points
        print(Max, "from savescores")"""


    def directory(self):
        global Ships
        Ships = get_ships(random=False)
        print(Ships, end ="\n\n")


    def full_random(self):
        global Ships
        Ships = get_ships(random=True)
        print(Ships, end='\n\n')


if __name__ == "__main__":
    MyMainApp().run()
