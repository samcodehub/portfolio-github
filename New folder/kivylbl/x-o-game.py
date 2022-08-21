# base class of your app inherite from app class app always refers to the instance of your application
from kivy.app import App

# boxlayout arranges children in a virtual or horizontal box
from kivy.uix.boxlayout import BoxLayout

# the gridlayout arranges children in a matrix, it takes the available space and divides it into columns and rows then adds widgets to the resulting cells
from kivy.uix.gridlayout import GridLayout

# the button is a label with asspciated actions that are triggered when the button is pressed or released after a click or touch
from kivy.uix.button import Button

# to change the default setting in kivy we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# the label widget is for rendering text
from kivy.uix.label import Label

# core class for creating the default kivy window setting
from kivy.core.window import Window
Window.clearcolor = (0, .2, .2, .1)

# to choose the numbers randomly every time you run it shows different numbers
import random

# importing time module
import time

# creating a class to declare the possible wining coordinates in x for horizotal, y for vertical and d for crossing
class GameApp(App):
    def tic_tac(self, arg):
        arg.disabled = True
        arg.text = "X"
        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )
        vector = (
            [self.button[x].text for x in (0, 1, 2)],
            [self.button[x].text for x in (3, 4, 5)],
            [self.button[x].text for x in (6, 7, 8)],
            [self.button[y].text for y in (0, 3, 6)],
            [self.button[y].text for y in (1, 4, 7)],
            [self.button[y].text for y in (2, 5, 8)],
            [self.button[d].text for d in (0, 4, 8)],
            [self.button[d].text for d in (2, 4, 6)],
        )
        win = False
        color = [.10, .64, .81, 1]
        for index in range(8):
            if vector[index].count('X') == 3:
                win = True
                self.a.text = str(int(self.a.text)+1)
                for i in coordinate[index]:
                    self.button[i].color = color
                break
            elif vector [index].count('O') == 3:
                win = True
                self.b.text = str(int(self.b.text)+1)
                for i in coordinate[index]:
                    self.button[i].color = color
                break
        # permitting the app to choose a number randomly and game rules
        ran = random.randint(0,8)
        if len(str(self.button[index].text)) == 1 or\
        len(str(self.button[index].text)) == 0:
            print("= 1")
            self.button[ran].text = "O"
            self.button[ran].disabled = True
        elif len(str(self.button[index].text)) == 0 or\
        len(str(self.button[ran].text)) == 0:
            print("= 0")
            if self.button[ran] == self.button[8]:
                print("!= 8")
                self.button[ran].text = ""
                self.button[ran].disabled = False
                self.button[0].text = "O"
                self.button[0].disabled = True
            else:
                self.button[ran+1].text ="0"
                self.button[ran+1].disabled = True
        if win:
            for index in range(9):
                self.button[index].disabled = True
    # restart function to restart the game
    def restart(self,arg):
        global switch; switch = 0
        for index in range(9):
            self.button[index].color = [.2, 0, 0, 1]
            self.button[index].text = ""
            self.button[index].disabled = False
    # new game function will remove all results and return the result as 0,0
    def new_game(self,arg):
        self.a.text = "0"
        self.b.text = "0"
        global switch; switch = 0
        for index in range(9):
            self.button[index].color = [.1, 0, .42, 1]
            self.button[index].text = ""
            self.button[index].disabled = False
    # using build function to create the restart and new game buttons and result labels also arrange the children using box and grid layout 
    def build(self):
        self.title = "X-O"
        root = BoxLayout(orientation = 'vertical', padding = 7)
        grid = GridLayout(cols = 3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(background_color = [1,0,0,.5], font_size = 35, disabled = False, on_press = self.tic_tac)
            grid.add_widget(self.button[index])
        lbls = BoxLayout(orientation = "horizontal", size_hint = (1, .11))
        self.a = Label(text = "0", size_hint = (1, .9), font_size = 27)
        self.b = Label(text = "0", size_hint = (1, .9), font_size = 27)
        lbls.add_widget(self.a)
        lbls.add_widget(self.b)
        root.add_widget(grid)
        root.add_widget(Button(text="Restart", background_color = (1, .6, 0, 1), size_hint=[1, .1], on_press = self.restart))
        root.add_widget(Button(text="New Game", background_color = (.5, 1, .7, 1), size_hint = [1, .1], on_press = self.new_game))
        root.add_widget(lbls)
        return root
# run the app
if __name__ == "__main__":
    GameApp().run()