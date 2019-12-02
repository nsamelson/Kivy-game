from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Wreck=[]
Copy=[]
Sunk=[]
Carrier = ["b2","b3","b4","b5","b6"]
Cruiser = ["a9","b9","c9","d9"]
Submarine1 = ["h8","i8","j8"]
Submarine2 = ["h1","h2","h3"]
Torpedo = ["e2","e3"]
Ships = [Carrier, Cruiser, Submarine1, Submarine2, Torpedo]

class ImageButton(ButtonBehavior,Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = 'blue.png'




    def on_press(self):
        self.source = "blue2.png"
        self.disabled = True
        #self.Counter()


        for ship in Ships:
            for xy in ship:
                if self.group == xy:
                    print(" ship touched in :", xy)
                    self.source = "red.png"
                    ord = ship.index(xy)
                    ship.pop(ord)
                    Wreck.append(xy)
            if len(ship) == 0:
                Copy = Wreck.copy()
                Sunk.append(Copy)

                if len(Wreck) ==2:
                    print("The Torpedo in :", Wreck, "has sunk")
                elif len(Wreck) ==3:
                    print("One of the two submarines in :", Wreck, "has shunk")
                elif len(Wreck) ==4:
                    print("The Cruiser in :", Wreck, "has shunk")
                elif len(Wreck) ==5:
                    print("The Carrier in :", Wreck, "has shunk")
                Wreck.clear()
                sunk = Ships.index(ship)
                Ships.pop(sunk)


    def on_release(self):
        if len(Ships) ==0:
            print("Touché coulé")
            exit()


class Counter(FloatLayout):
    def counter(self, moves, score):
        moves.text = (str(int(moves.text) + 1))
        score.text = str(1700 / int(moves.text)) if int(moves.text) > 17 else str(100 * int(moves.text) / 17)




def show_popup():
    show = P()
    popWindow = Popup(title="Scores", content=show, size_hint=(None,None), size =(500,500))
    popWindow.open()
class P(FloatLayout):
    pass

class ToggleButton(ToggleButtonBehavior):
    pass

class FirstWindow(Screen):          #ecran de bienvenue
    pass

class SecondWindow(Screen):            #ecran de scores en popup et options
    def btn3(self):
        show_popup()

class ThirdWindow(Screen,FloatLayout):              #ecran pour entrer son nom et lancer le jeu
    pass

class FourthWindow(Screen):            #ecran joueur 1 en duel
    pass

class Player2Window(Screen):            #ecran joueur 2 en duel
    pass

class TransitionWindow(Screen):         #ecran de transition entre le joueur 1 et 2
    pass




class WindowManager(ScreenManager):
    pass














kv = Builder.load_file("my.kv")

class MyMainApp (App):
    def build(self):
        return kv




if __name__ == "__main__":
    MyMainApp().run()