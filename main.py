from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,NumericProperty, ListProperty)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

import json
import os

Alpha =["A","B","C","D","E","F","G","H","I","J"]
Wreck=[]
Copy=[]
Sunk=[]
Sunkships =[]
Bingo = []
Carrier = ["B2","B3","B4","B5","B6"]
Cruiser = ["A9","B9","C9","D9"]
Submarine1 = ["H8","I8","J8"]
Submarine2 = ["H1","H2","H3"]
Torpedo = ["E2","E3"]
Ships = [Carrier, Cruiser, Submarine1, Submarine2, Torpedo]
ScoTab =[]
class WindowManager (ScreenManager):
    pass
class FirstWindow (Screen):
    pass
class SecondWindow (Screen):
    pass
class ThirdWindow (Screen):
    pass

class FourthWindow (Screen):
    def on_pre_enter(self):
        Window.size = (1150, 500)
    def on_pre_leave(self):
        Window.size = (800, 600)
class FifthWindow (Screen,GridLayout):
    player_name = StringProperty("")
    score = StringProperty('0')

    def on_pre_enter(self):
        MyMainApp.savescore(self)

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
    tab = ObjectProperty(None)

    def on_tab(self, *args):
        self.tab.add_widget(Label(text="Name:"))
        self.tab.add_widget(Label(text="Score out of 100 :"))
        for m in range(len(ScoTab)):
            self.tab.add_widget(Label(text=str(ScoTab[m])))
        print("test")




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
        filename = "result.json"
        jsonresult = {'player': self.player_name, 'score': self.score}
        print(jsonresult)

        if (os.path.isfile(filename)):
            # lecture des scores
            with open(filename, "r") as file:
                data = json.load(file)
        else:
            data = []


        # ajout d'un nouveau score
        if self.player_name!= "" or self.score != "0":
            data.append({'player': self.player_name, 'score': self.score})
        with open(filename, "w") as file:
            json.dump(data, file)
        while len(ScoTab) <= 15:
            for score in data:
                ScoTab.insert(0, score["score"])
                ScoTab.insert(0, score["player"])

        print(ScoTab)



if __name__ == "__main__":
    MyMainApp().run()
