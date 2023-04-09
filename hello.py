import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from decimal import Decimal

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
            
            Button:
                text: "CE"
                grid: (1, 0)

            Button:
                id: clear
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
                text: "7"
                grid: (0, 1)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(7)
            
            Button:
                text: "8"
                grid: (1, 1)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(8)


            Button:
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
                text: "4"
                grid: (0, 2)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(4)

                
            Button:
                text: "5"
                grid: (1, 2)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(5)
                
            Button:
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
                text: "1"
                grid: (0, 3)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(1)
                
            Button:
                text: "2"
                grid: (1, 3)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(2)
                
            Button:
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

                
            Button:
                text: "0"
                grid: (1, 4)
                background_color: 157/255, 157/255, 157/255, 1
                on_press: root.number_press(0)
                
            Button:
                text: "."
                text_color: 0, 0, 0, 1
                grid: (2, 4)
                background_color: 157/255, 157/255, 157/255, 1

            Button:
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

    def clear(self):
        self.ids.calc_input.text = "0"

    # define the equals function
    def equals(self):
        if self.active_operation == "addition":
            total = self.first_number + self.second_number
            self.ids.calc_input.text = str(total)
            self.active_operation = ""
            self.addition = False
            self.ids.addition_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "subtraction":
            total = self.first_number - self.second_number
            self.ids.calc_input.text = str(total)
            self.active_operation = ""
            self.subtraction = False
            self.ids.subtraction_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "multiplication":
            total = self.first_number * self.second_number
            self.ids.calc_input.text = str(total)
            self.active_operation = ""
            self.multiplication = False
            self.ids.multiplication_button.background_normal = "atlas://data/images/defaulttheme/button"

        elif self.active_operation == "division":
            total = self.first_number / self.second_number
            self.ids.calc_input.text = str(total)
            self.active_operation = ""
            self.division = False
            self.ids.division_button.background_normal = "atlas://data/images/defaulttheme/button"

    # Number button press
    def number_press(self, number):

        # if the first number is 0 then clear the text
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""

        # check if any of the operations are active
        if self.addition or self.subtraction or self.multiplication or self.division:
            # clear the text
            self.ids.calc_input.text = ""

        self.ids.calc_input.text += str(number)
        # limit the number of characters to fit the screen
        if len(self.ids.calc_input.text) > 15:
            self.ids.calc_input.text = self.ids.calc_input.text[:-1]

        # set the new input to true
        self.new_input = True

    # Operation button press
    def operation_press(self, operation):

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

    def equals_press(self):
        # set the second number
        self.second_number = Decimal(self.ids.calc_input.text)

        self.equals()
    

class MyApp(App):
    def build(self):
        Window.clearcolor = (200/255, 200/255, 200/255, 1)
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
