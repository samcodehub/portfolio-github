import kivy

kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.vkeyboard import VKeyboard
class Test(VKeyboard):
    player = VKeyboard()
class VKeyboardApp(App):
    def build(self):
        return Test()
if __name__ == "__main__":
    VKeyboard().run()