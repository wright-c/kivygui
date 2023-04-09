import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

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
                on_release: 
                    # keep the color of the button the same as it was while it was pressed
                    self.background_normal = self.background_down



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
                on_press: root.equals()

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

    def clear(self):
        self.ids.calc_input.text = "0"

    # Number button press
    def number_press(self, number):
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

    # Add button press
    def operation_press(self, operation):
        # if the text is 0 then set it to nothing
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""

        # if the first number is 0 then skip the rest of the function
        if self.first_number == 0:
            return

        # check operation and set the active operation
        if operation == "addition":
            self.active_operation = "addition"
            self.addition = True
            self.subtraction = False
            self.multiplication = False
            self.division = False
            # highlight the button
            self.ids.addition_button.background_color = 0, 0, 0, 1
            self.ids.addition_button.text_color = 1, 1, 1, 1

        elif operation == "subtraction":
            self.active_operation = "subtraction"
            self.addition = False
            self.subtraction = True
            self.multiplication = False
            self.division = False
            # highlight the button
            self.ids.subtraction_button.background_color = 0, 0, 0, 1
            self.ids.subtraction_button.text_color = 1, 1, 1, 1

        elif operation == "multiplication":
            self.active_operation = "multiplication"
            self.addition = False
            self.subtraction = False
            self.multiplication = True
            self.division = False
            # highlight the button

        elif operation == "division":
            self.active_operation = "division"
            self.addition = False
            self.subtraction = False
            self.multiplication = False
            self.division = True
            # highlight the button
            self.ids.division_button.background_color = 0, 0, 0, 1
            self.ids.division_button.text_color = 1, 1, 1, 1

    # Equals button press
    # def equals(self):


class MyApp(App):
    def build(self):
        Window.clearcolor = (200/255, 200/255, 200/255, 1)
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
