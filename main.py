from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

#BasicApp inherits properties of App
class BasicApp(App): 
    def build(self):
        #makes a layout with padding around it
        layout = BoxLayout(padding=10)
        label = Label(text="Hello world")
        #always has to return root widget
        layout.add_widget(label)
        return layout


app = BasicApp()
app.run()