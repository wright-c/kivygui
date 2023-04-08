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

<Button>:
    text_color: 1, 1, 1, 1
    border: 1, 1, 1, 1

<MyLayout>
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    

    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height

        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            font_size: 65
            size_hint: 1, .15

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
                text: "C"
                grid: (2, 0)

            Button:
                text: "/"
                grid: (3, 0)

            # Row 2
            Button:
                text: "7"
                grid: (0, 1)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1
            
            Button:
                text: "8"
                grid: (1, 1)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "9"
                grid: (2, 1)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "x"
                grid: (3, 1)


            # Row 3
            Button:
                text: "4"
                grid: (0, 2)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "5"
                grid: (1, 2)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "6"
                grid: (2, 2)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "-"
                grid: (3, 2)

            # Row 4
            Button:
                text: "1"
                grid: (0, 3)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1
            
            Button:
                text: "2"
                grid: (1, 3)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "3"
                grid: (2, 3)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "+"
                grid: (3, 3)

            # Row 5
            Button:
                text: "+/-"
                grid: (0, 4)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "0"
                grid: (1, 4)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1

            Button:
                text: "."
                text_color: 0, 0, 0, 1
                grid: (2, 4)
                background_normal: ""
                background_color: 240/255, 240/255, 240/255, 1
                border: 1, 1, 1, 1

            Button:
                text: "="
                grid: (3, 4)
                background_normal: ""
                background_color: 100/255, 100/255, 100/255, 1


''')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (200/255, 200/255, 200/255, 1)
        return MyLayout()    
if __name__ == '__main__':
    MyApp().run()