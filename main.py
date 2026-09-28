import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

#BasicApp inherits properties of App
# Window.clearcolor = (1, 1, 1, 1)

# class ShumBody(Widget):
#     #  def __init__(self, **kwargs):
          
#     # def onClick():
#     #     return 1
#     pass

class ShumScreen(Screen):
    def change_screen(self):
        self.manager.current = "Home"
        print("yep")

class HomeScreen(Screen):
    def change_screen(self): #put in extra variable that shows which screen it will change to
        self.manager.current = "WhoIsShum"
        print("yop")

class MyScreenManager(ScreenManager):
    pass

class ShumUIApp(App): 
    def build(self):
        # #makes a layout with padding around it
        # layout = BoxLayout(padding=10)
        # label = Label(text="Hello world")
        # an_image = Image(source='public/shumHIMSELF.png')
        # button = Button(text='a button')
        # button.bind(on_press=ShumUIApp.callback)
        # #always has to return root widget

        # layout.add_widget(an_image)  
        # layout.add_widget(label)
        # layout.add_widget(button)
        # layout.add_widget(ShumBody()) #does work
        # return layout
        return MyScreenManager()
    # def callback(instance):
    #     print('My button <%s>' % (instance))
        
        


app = ShumUIApp()
app.run()