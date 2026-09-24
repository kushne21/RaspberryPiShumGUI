import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

#BasicApp inherits properties of App

class ShumBody(Widget):
    def onClick():
        return 1
    

class BasicApp(App): 
    def build(self):
        #makes a layout with padding around it
        layout = BoxLayout(padding=10)
        label = Label(text="Hello world")
        an_image = Image(source='public/shumHIMSELF.png')
        #always has to return root widget

        layout.add_widget(an_image)  
        layout.add_widget(label)
        return layout
        
        


app = BasicApp()
app.run()