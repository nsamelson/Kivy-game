from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,NumericProperty, ListProperty)
from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


Alpha =["A","B","C","D","E","F","G","H","I","J"]
Wreck=[]
Copy=[]
Sunk=[]
Sunkships =[]

Carrier = ["B2","B3","B4","B5","B6"]
Cruiser = ["A9","B9","C9","D9"]
Submarine1 = ["H8","I8","J8"]
Submarine2 = ["H1","H2","H3"]
Torpedo = ["E2","E3"]
Ships = [Carrier, Cruiser, Submarine1, Submarine2, Torpedo]

class WindowManager (ScreenManager):
    pass
class FirstWindow (Screen):
    pass
class SecondWindow (Screen):
    pass
class ThirdWindow (Screen):
    def on_leave(self): # Trying to reset the game so I can replay it without quitting and restarting

        self.clear_widgets()
    def on_enter(self):
       # self.add_widget(Counter.counter((self, counter.moves()), score ,sink))
        Counter.counter(self,moves=0,score=0,sink="")   # I don't know what to put


class FourthWindow (Screen):
    pass

class Counter(GridLayout):
    def counter(self, moves, score,sink):
        sink.text = str("\n".join(Sunkships))   #It's for telling which ship has been sunk. I have also an issue with it where I must click another button to activate it and show the ship that sank
        moves.text = (str(int(moves.text) + 1))
        score.text = str("%.2f"% (1700 / int(moves.text)) if int(moves.text) > 17 else str("%.2f"%(100 * int(moves.text) / 17)))




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

class ImageButton(ButtonBehavior,Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'blue.png'

    #box = ObjectProperty(None) pour essayer de clear la grille


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
            #self.clear_party()

    def popopen(self):
        popsave = Pop()
        popsave.open()
        #scores.text = Counter.counter.score.text
    def clear_party(self):

        MyWidget.__init__(self)





            #save_score()               #trying to show the popup to save score


class Pop (Popup):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp (App):
    def build(self):
        return kv



    def save_score(self):
        pass
    def schow_score(self):
        pass

if __name__ == "__main__":
    MyMainApp().run()