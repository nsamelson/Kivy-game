from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button



Wreck=[]
Copy=[]
Sunk=[]


Submarine2 = ["a3"]
Torpedo = ["a1","a2"]

Ships = [Submarine2, Torpedo]

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
                print("the ship in",Wreck, "has sunk")
                Wreck.clear()
                sunk = Ships.index(ship)
                Ships.pop(sunk)


    def on_release(self):
        if len(Ships) ==0:
            print("Touché coulé")
            #breakpoint()


class Counter(FloatLayout):
    def counter(self, moves, score):
        moves.text = (str(int(moves.text) + 1))
        score.text = str(17000) / int(moves.text) if int(moves.text) > 17 else str(100 * int(moves.text) / 17)



class MyGrid(FloatLayout):
    pass

class MyApp (App):                                      # lance l'app "MyApp"
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
