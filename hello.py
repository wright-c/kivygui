import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('hello.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    colour = ObjectProperty(None)
    
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        colour = self.colour.text

        # Print to a label at the end of the screen
        #self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, and your favourite color is {color}"))

        # Print to the console
        print(f"Hello {name}, you like {pizza} pizza, and your favourite color is {colour}")

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.colour.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()    
if __name__ == '__main__':
    MyApp().run()