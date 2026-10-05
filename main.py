import kivy

import os

# 1. Disable multi-touch emulation red dots 
os.environ["KIVY_NO_ARGS"] = "1"

# 2. Set the configuration before any other Kivy imports
from kivy.config import Config

# Set viewport width and height (e.g., iPhone 12/13 Pro size: 390x844)
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "480")

# Prevent the user from resizing the window during the test
Config.set("graphics", "resizable", "0")
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
#BasicApp inherits properties of App
Window.clearcolor = (1, 1, 1, 1)



class ShumScreen(Screen):
    def change_screen(self):
        self.manager.current = "HomeScreen"

class ShumWidget(Image):
    def on_touch_down(self, touch):
        # 1. Check if the click/touch happened inside the image boundaries
        if self.collide_point(*touch.pos):
            with self.canvas:
                # 2. Set the drawing color (e.g., Red)
                Color(0, 0, 0, 1) 
                
                # 3. Create a starting point line
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)
            
            # Allow the touch to propagate if needed
            return True
        return True
        return super(ShumWidget, self.on_touch_down)(touch)

    def on_touch_move(self, touch):
        # 4. Drag to draw lines if the initial touch was valid
        if self.collide_point(*touch.pos) and 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]
            return True
        return True
        return super(ShumWidget, self.on_touch_move)(touch)

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        # Pass the screen name to the parent Screen class
        super().__init__(name="HomeScreen", **kwargs)
    
    
    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)
        # Create the BoxLayout
        self.clear_widgets()
        layout = BoxLayout(orientation='horizontal')
        
        # 1. Create the image widget
        img = ShumWidget(source='./public/shumHIMSELF.png')
        
        
        
        # 3. Bind the widget size to the image file's actual size
        img.bind(texture_size=img.setter('size'))
        layout.add_widget(img)
        rightlayout = BoxLayout(orientation='vertical')
        rightlayout.add_widget(Label(text='What would you like to know about Shum?', color = [0,0,0,1], bold=True, font_size='20sp'))
        rightlayout = self.MakeButtons(rightlayout)
        layout.add_widget(rightlayout)

        # Add the layout to the screen
        self.add_widget(layout)

    def AddButton(self, strquestion, strans, layout):
        outerlayout = BoxLayout(padding=15)
        z= random.uniform(0.1, 1) 
        b = random.uniform(0.1, 1) 
        e = random.uniform(0.1, 1) 
        button = Button(border=[30,30,30,30],text=strquestion, bold=True, background_normal='',background_color=[z, b, e, 0.2],  color = [z,b,e,1], font_size = '20sp', halign='center', valign='center')
        button.bind(size=lambda instance, size: setattr(instance, 'text_size', (size[0], None)))
        button.bind(on_press=lambda instance: self.change_screen(strans))
        outerlayout.add_widget(button)
        layout.add_widget(outerlayout)
        return layout
    
    def MakeRandom(self, randoms):
        random_pair = random.choice(list(randoms.items()))
        other_rand = random.choice(list(randoms.items()))
        while(other_rand == random_pair):
            other_rand = random.choice(list(randoms.items()))
        return (random_pair, other_rand)
        
        #add 5 buttons to the layout, last 2 random and each going to the other screen
    def MakeButtons(self, layout):
        essentials={
                    "Who is Shum?": "Shum is a plant fertility god and the central messianic figure of the religion Shumblism. Unlike certain other religions, you may worship his icon. \n Shum was born millions of years ago in South America, with his brother Loba, a lobster. \n Shum, with his unending love, gifted the Lobster sentience and knowledge. \n Shum once had a tail, but was cut off by Loba and fell unto the world, birthing the Amazon. \n Shum is within all green in the world, Shum is our love, Shum is within us.",
                    "What do these paintings even mean? How do they relate to Shum?" : "The paintings are all about deception.\n They are all lying to you.\n They're putting you on.\n You have to figure them out.\n \n Shum is in everything.",
                    "How can I contact you (Ashton Kushner) or see more of your art?": "Go to my website: \n ashtonkushner.com"
                }
        randoms={
                    "Well what does the snail one mean?":"The painting \"Midwestern Snome (Advertisement)\" is about commercials and advertisements. In my experience, commercials tend to have mysterious or otherwise nonsensical plots, for example a medicine advertisement with the visuals being completely unrelated. Here, I've taken a topic to advertise: the midwestern United States. \n \n I've pared down the idea of the midwest to a random, specific stereotype: cornfields.Thus, you have a simple agrarian scene, but of course it also needs characters, that being two gnomes. These were added arbitrarily, but I've chosen the foreground gnome to be a snail with a warm smile to be more inviting to the viewer. \n \n Other aspects of the scene are there to evoke advertisement-like imagery, the clouds acting as slot machines or the floating state-shaped dollars to evoke the feeling of monetary gain from this place. Because the image only loosely resembles the midwest, and claims to be of the midwest, the purpose of deception and giving you the urge to buy a service because of an icon fulfills its role within the exhibition. Of course, because of the red-yellow flower, you can assume a certain Being resides within the painting.",
                    "Is Shum supposed to be Jesus?" : "Shum is not related to any figure from any other religion. \n Shumblism is not a critique or parody of any major religion, but you may interpret it as a critique of cults such as Scientology if you wish.",
                    "How do I convert to Shumblism?" : "Ask Shum.",
                    "Who is the old lady in that painting?" : "Ask Shum.",
                    "What is the Church of Shum?" : "The Church of Shum is the world's only church dedicated to Shum. You can go to www.churchofshum.org to learn more.",
                    "Why is this exhibition called The Simulacrum of Shum?": "From Wikipedia: \n A simulacrum (pl.: simulacra or simulacrums, from Latin simulacrum, meaning 'likeness, semblance') is a representation or imitation of a person or thing. The word was first recorded in the English language in the late 16th century, used to describe a representation, such as a statue or a painting, especially of a god. By the late 19th century, it had gathered a secondary association of inferiority: an image without the substance or qualities of the original."
                }
                
        the_random_choices = self.MakeRandom(randoms)
        for key, value in essentials.items():
            layout = self.AddButton(key, value, layout)
        for key, value in the_random_choices:
            layout = self.AddButton(key, value, layout)
        return layout

    def change_screen(self, strans): #put in extra variable that shows which screen it will change to
        
        self.manager.get_screen('ShumScreen').ids.the_button.text = strans
        self.manager.current = "ShumScreen"
        print("yop")

class MyScreenManager(ScreenManager):
    pass

class ShumUIApp(App): 
    
    

    def build(self):
        
        return MyScreenManager(transition=NoTransition())
   


app = ShumUIApp()
app.run()