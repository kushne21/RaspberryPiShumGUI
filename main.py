import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

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
    def AddButton(self, strquestion, strans):
        
        pass
    def MakeRandom(self, randoms):
        random_pair = random.choice(list(randoms.items()))
        other_rand = random.choice(list(randoms.items()))
        while(other_rand == random_pair):
            other_rand = random.choice(list(randoms.items()))
        return (random_pair, other_rand)
    
    def MakeButtons(self,essentials, randoms):
        the_random_choices = self.MakeRandom(randoms)
        for key, value in essentials:
            self.AddButton(key, value)
        for key, value in randoms:
            self.AddButton(key, value)

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
        essentials={
            "Who is Shum?": "Shum is a plant fertility god and the central messianic figure of the religion Shumblism. Unlike certain other religions, you may worship his icon. \n Shum was born millions of years ago in South America, with his brother Loba, a lobster. \n Shum, with his unending love, gifted the Lobster sentience and knowledge. \n Shum once had a tail, but was cut off by Loba and fell unto the world, birthing the Amazon. \n Shum is within all green in the world, Shum is our love, Shum is within us.",
            "What do these paintings even mean? How do they relate to Shum?" : "The paintings are all about deception. They are all lying to you. They're putting you on. You have to figure them out. \n Shum is in everything.",
            "How can I contact you (Ashton Kushner) or see more of your art?": "Go to my website: \n ashtonkushner.com"
        }
        randomquestions={
            "Well what does the snail one mean?":"The painting \"Midwestern Snome (Advertisement)\" is about commercials and advertisements. In my experience, commercials tend to have mysterious or otherwise nonsensical plots, for example a medicine advertisement with the visuals being completely unrelated. Here, I've taken a topic to advertise: the midwestern United States. \n I've pared down the idea of the midwest to a random, specific stereotype: cornfields.Thus, you have a simple agrarian scene, but of course it also needs characters, that being two gnomes. These were added arbitrarily, but I've chosen the foreground gnome to be a snail with a warm smile to be more inviting to the viewer. \n Other aspects of the scene are there to evoke advertisement-like imagery, the clouds acting as slot machines or the floating state-shaped dollars to evoke the feeling of monetary gain from this place. Because the image only loosely resembles the midwest, and claims to be of the midwest, the purpose of deception and giving you the urge to buy a service because of an icon fulfills its role within the exhibition. Of course, because of the red-yellow flower, you can assume a certain Being resides within the painting.",
            "Is Shum supposed to be Jesus?" : "Shum is not related to any figure from any other religion. \n Shumblism is not a critique or parody of any major religion, but you may interpret it as a critique of cults such as Scientology if you wish.",
            "How do I convert to Shumblism?" : "Ask Shum.",
            "Who is the old lady in that painting?" : "Ask Shum.",
            "What is the Church of Shum?" : "The Church of Shum is the world's only church dedicated to Shum. You can go to www.churchofshum.org to learn more.",
            "Why is this exhibition called The Simulacrum of Shum?": "From Wikipedia: \n A simulacrum (pl.: simulacra or simulacrums, from Latin simulacrum, meaning 'likeness, semblance') is a representation or imitation of a person or thing. The word was first recorded in the English language in the late 16th century, used to describe a representation, such as a statue or a painting, especially of a god. By the late 19th century, it had gathered a secondary association of inferiority: an image without the substance or qualities of the original."
        }
        
        self.MakeButtons(essentials, randomquestions)
        return MyScreenManager(transition=NoTransition())
    # def callback(instance):
    #     print('My button <%s>' % (instance))
        
        


app = ShumUIApp()
app.run()