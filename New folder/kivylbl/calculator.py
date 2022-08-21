# base class of your app inherite from app class always refer to the instance of your application
from kivy.app import App

# to change the default setting in kivy we use config
from kivy.config import Config
Config.set('graphics','width','500')
Config.set('graphics','height','500')

# boxlayout arranges children in a vertical or horizontal box
from kivy.uix.boxlayout import BoxLayout

# the button is a label with associated actions that are triggered when the button is pressed(or released after a click/touch)
from kivy.uix.button import Button

# the textinput widget provides a box for editable plain text
from kivy.uix.textinput import TextInput

# create the main class of calculator 
class CalcApp(App):
    def build(self):
        # declaring the operators 
        self.operators = ["/","*","+","-"]
        self.last_was_operator = None
        self.last_button = None
        # arranging the children and create the textinput
        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(
            multiline = False, readonly=True, halign= "right", font_size = 55, background_color = (0, 1, .5, 1)
            
        )
        # adding all widgets and buttons in rows
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9","/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label,
                    pos_hint = {"center_x": 0.5, "center_y": 0.5}, background_color = (.5, 1, 1, 1)
                    
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        # creating the equal button
        equals_button = Button(
            text = "=", font_size = 30, background_color = (.5, .8, 1, 1), pos_hint={"center_x": 0.5, "center_y": 0.5}
             
        ) 
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout
    # using on_button_press function to give functionality to the buttons
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
        # clear the solution widget
           self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators
            ):
                # dont add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # first character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    # a function to show the result
    def on_solution(self, instance):
        text = self.solution.text
        
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
            
# run the app
if __name__ == "__main__":
    app = CalcApp()
    app.run()
    
    
    

        
                