import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from decimal import Decimal
from kivy.logger import Logger
from kivy.clock import Clock
# import keyboard
import keyboard as kb


Window.size = (500, 700)


Builder.load_string(''' 

<MyLayout>

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

        TextInput:
            id: calc_input
            multiline: False
            text: "0"
            halign: "right"
            font_size: 105
            # make the size only the height of the text
            size_hint_y: None
            height: 150
            

        GridLayout:
            cols: 4
            rows: 5
            size: root.width, root.height

            # Row 1
            Button:
                text: "%"
                grid: (0, 0)
                on_press: root.percentage_press()
            
            Button:
                id: clear_entry_button
                text: "CE"
                grid: (1, 0)
                on_press: root.clear_entry()

            Button:
                id: clear_button
                text: "C"
                grid: (2, 0)
                on_press: root.clear()

            Button:
                id: division_button
                text: "/"
                grid: (3, 0)
                on_press: root.operation_press("division")

            # Row 2
            Button:
                id : number_7_button
                text: "7"
                grid: (0, 1)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(7)
            
            Button:
                id: number_8_button
                text: "8"
                grid: (1, 1)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(8)


            Button:
                id: number_9_button
                text: "9"
                grid: (2, 1)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(9)

            Button:
                id: multiplication_button
                text: "x"
                grid: (3, 1)
                on_press: root.operation_press("multiplication")


            # Row 3
            Button:
                id: number_4_button
                text: "4"
                grid: (0, 2)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(4)

                
            Button:
                id: number_5_button
                text: "5"
                grid: (1, 2)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(5)
                
            Button:
                id: number_6_button
                text: "6"
                grid: (2, 2)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(6)
                
            Button:
                id: subtraction_button
                text: "-"
                grid: (3, 2)
                on_press: root.operation_press("subtraction")

            # Row 4
            Button:
                id: number_1_button
                text: "1"
                grid: (0, 3)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(1)
                
            Button:
                id: number_2_button
                text: "2"
                grid: (1, 3)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(2)
                
            Button:
                id: number_3_button
                text: "3"
                grid: (2, 3)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(3)
                
            Button:
                id: addition_button
                text: "+"
                grid: (3, 3)
                on_press: root.operation_press("addition")

            # Row 5
            Button:
                text: "+/-"
                grid: (0, 4)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.positive_negative_press()

                
            Button:
                id: number_0_button
                text: "0"
                grid: (1, 4)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(0)
                
            Button:
                id: decimal_button
                text: "."
                text_color: 0, 0, 0, 1
                grid: (2, 4)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.decimal_press()

            Button:
                id: equals_button
                text: "="
                grid: (3, 4)
                on_press: root.equals_press()

''')


class MyLayout(Widget):

    # properties
    # if addition, subtraction, multiplication, or division is pressed then set the active_operation to the operation
    addition = False
    subtraction = False
    multiplication = False
    division = False
    active_operation = ""
    first_number = 0
    second_number = 0
    total = 0
    new_input = False
    new_equation = True

    def clear(self):
        self.ids.calc_input.text = "0"

        # set all the operations to false
        self.addition = False
        self.subtraction = False
        self.multiplication = False
        self.division = False

        # set the active operation to nothing
        self.active_operation = ""

        # set the first, second and total numbers to 0
        self.first_number = 0
        self.second_number = 0
        self.total = 0

        # set the new input to true
        self.new_input = True

        # set the new equation to true
        self.new_equation = True

        # set the background color of the buttons to normal
        self.ids.addition_button.background_normal = "atlas://data/images/defaulttheme/button"
        self.ids.subtraction_button.background_normal = "atlas://data/images/defaulttheme/button"
        self.ids.multiplication_button.background_normal = "atlas://data/images/defaulttheme/button"
        self.ids.division_button.background_normal = "atlas://data/images/defaulttheme/button"

    # define the CE function
    def clear_entry(self):

        # set the input text to 0
        self.ids.calc_input.text = "0"

        # set the new input to true
        self.new_input = True

    # define the equals function
    def equals(self):
        if self.active_operation == "addition":
            self.total = self.first_number + self.second_number
            self.ids.calc_input.text = str(self.total)
            self.first_number = self.total
            self.active_operation = ""
            self.addition = False
            self.ids.addition_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "subtraction":
            self.total = self.first_number - self.second_number
            self.ids.calc_input.text = str(self.total)
            self.first_number = self.total
            self.active_operation = ""
            self.subtraction = False
            self.ids.subtraction_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "multiplication":
            self.total = self.first_number * self.second_number
            self.ids.calc_input.text = str(self.total)
            self.first_number = self.total
            self.active_operation = ""
            self.multiplication = False
            self.ids.multiplication_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "division":
            self.total = self.first_number / self.second_number
            self.ids.calc_input.text = str(self.total)
            self.first_number = self.total
            self.active_operation = ""
            self.division = False
            self.ids.division_button.background_normal = "atlas://data/images/defaulttheme/button"

        # set the new input to true
        self.new_input = True

    # Number button press
    def number_press(self, number):

        # if the first number is 0 then clear the text
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""

        # check if the new input is false, if it is then clear the text
        if not self.new_input:
            self.ids.calc_input.text = ""

        # if the user finishes an operation and presses a number then clear the text, and set variables to 0 in order to start a new operation
        if self.total != 0 and self.new_input and self.new_equation:
            self.ids.calc_input.text = ""
            self.first_number = 0
            self.second_number = 0
            self.total = 0

        self.ids.calc_input.text += str(number)
        # limit the number of characters to fit the screen
        if len(self.ids.calc_input.text) > 15:
            self.ids.calc_input.text = self.ids.calc_input.text[:-1]

        # set the new input to true
        self.new_input = True

    # Decimal button press
    def decimal_press(self):

        # check if the new input is false, if it is then clear the text
        if not self.new_input:
            self.ids.calc_input.text = ""

        # if the user finishes an operation and presses a number then clear the text, and set variables to 0 in order to start a new operation
        if self.total != 0 and self.new_input and self.new_equation:
            self.ids.calc_input.text = ""
            self.first_number = 0
            self.second_number = 0
            self.total = 0

        # if the text box does not contain a decimal then add one
        if "." not in self.ids.calc_input.text:
            self.ids.calc_input.text += "."

        # set the new input to true
        self.new_input = True

    # Operation button press
    def operation_press(self, operation):

        # set new operation to false
        self.new_equation = False

        # if the first number is not 0 then set the second number to the current number in the text box and run the equals function
        if self.first_number != 0 and self.new_input:
            self.second_number = Decimal(self.ids.calc_input.text)
            self.equals()

        # set the first number
        self.first_number = Decimal(self.ids.calc_input.text)

        # if the first number is 0 then skip the rest of the function
        if self.first_number == 0:
            return

        if self.active_operation != "":
            self.ids.addition_button.background_normal = "atlas://data/images/defaulttheme/button"
            self.ids.subtraction_button.background_normal = "atlas://data/images/defaulttheme/button"
            self.ids.multiplication_button.background_normal = "atlas://data/images/defaulttheme/button"
            self.ids.division_button.background_normal = "atlas://data/images/defaulttheme/button"

        # set the new input to false
        self.new_input = False

        # check operation and set the active operation
        if operation == "addition":

            # set the active operation to addition
            self.active_operation = "addition"
            self.addition = True
            self.subtraction = False
            self.multiplication = False
            self.division = False

            # change the button color to show that it is active
            self.ids.addition_button.background_normal = "atlas://data/images/defaulttheme/button_pressed"

        elif operation == "subtraction":

            # set the active operation to subtraction
            self.active_operation = "subtraction"
            self.addition = False
            self.subtraction = True
            self.multiplication = False
            self.division = False

            # change the button color to show that it is active
            self.ids.subtraction_button.background_normal = "atlas://data/images/defaulttheme/button_pressed"

        elif operation == "multiplication":

            # set the active operation to multiplication
            self.active_operation = "multiplication"
            self.addition = False
            self.subtraction = False
            self.multiplication = True
            self.division = False

            # change the button color to show that it is active
            self.ids.multiplication_button.background_normal = "atlas://data/images/defaulttheme/button_pressed"

        elif operation == "division":

            # set the active operation to division
            self.active_operation = "division"
            self.addition = False
            self.subtraction = False
            self.multiplication = False
            self.division = True

            # change the button color to show that it is active
            self.ids.division_button.background_normal = "atlas://data/images/defaulttheme/button_pressed"

    # positive/negative button press
    def positive_negative_press(self):

        # if the text box is not empty then change the number to positive or negative
        if self.ids.calc_input.text != "":
            if self.ids.calc_input.text[0] == "-":
                self.ids.calc_input.text = self.ids.calc_input.text[1:]
            else:
                self.ids.calc_input.text = "-" + self.ids.calc_input.text

    def equals_press(self):
        # set the second number
        self.second_number = Decimal(self.ids.calc_input.text)

        self.equals()
        self.new_equation = True
        self.new_input = True

    # define the percentage function
    def percentage_press(self):
        # if the text box is not empty then calculate the percentage
        if self.ids.calc_input.text != "":
            self.ids.calc_input.text = str(
                Decimal(self.ids.calc_input.text) / 100)


class MyApp(App):
    def build(self):
        Window.clearcolor = (200/255, 200/255, 200/255, 1)
        return MyLayout()

    def on_start(self):
        Window.bind(on_keyboard=self.on_keyboard)

    # define a fucntion to check if a key is pressed, if so trigger the corresponding button press
    def on_keyboard(self, window, key, scancode, codepoint, modifier):

        print(f"{key} was pressed")

        # if key is an int
        if type(key) == int:

            # num pad 1 and regular 1
            if key == 257 or key == 49:
                button = App.get_running_app().root.ids.number_1_button
                button.trigger_action()
            # num pad 2 and regular 2
            elif key == 258 or key == 50:
                button = App.get_running_app().root.ids.number_2_button
                button.trigger_action()
            # num pad 3 and regular 3
            elif key == 259 or key == 51:
                button = App.get_running_app().root.ids.number_3_button
                button.trigger_action()
            # num pad 4 and regular 4
            elif key == 260 or key == 52:
                button = App.get_running_app().root.ids.number_4_button
                button.trigger_action()
            # num pad 5 and regular 5
            elif key == 261 or key == 53:
                button = App.get_running_app().root.ids.number_5_button
                button.trigger_action()
            # num pad 6 and regular 6
            elif key == 262 or key == 54:
                button = App.get_running_app().root.ids.number_6_button
                button.trigger_action()
            # num pad 7 and regular 7
            elif key == 263 or key == 55:
                button = App.get_running_app().root.ids.number_7_button
                button.trigger_action()
            # num pad 8 and regular 8
            elif key == 264 or key == 56:
                button = App.get_running_app().root.ids.number_8_button
                button.trigger_action()
            # num pad 9 and regular 9
            elif key == 265 or key == 57:
                button = App.get_running_app().root.ids.number_9_button
                button.trigger_action()
            # num pad 0 and regular 0
            elif key == 256 or key == 48:
                button = App.get_running_app().root.ids.number_0_button
                button.trigger_action()
            # num pad . and regular .
            elif key == 266 or key == 46:
                button = App.get_running_app().root.ids.decimal_button
                button.trigger_action()
            # num pad enter and regular enter
            elif key == 271 or key == 13:
                button = App.get_running_app().root.ids.equals_button
                button.trigger_action()
            # num pad +
            elif key == 270:
                button = App.get_running_app().root.ids.addition_button
                button.trigger_action()
            # num pad -
            elif key == 269:
                button = App.get_running_app().root.ids.subtraction_button
                button.trigger_action()
            # num pad *
            elif key == 268:
                button = App.get_running_app().root.ids.multiplication_button
                button.trigger_action()
            # num pad /
            elif key == 267:
                button = App.get_running_app().root.ids.division_button
                button.trigger_action()
            # backspace
            # elif key == 8:
                # button = App.get_running_app().root.ids.clear_button
                # button.trigger_action()

        return True


if __name__ == '__main__':
    MyApp().run()
