from os import W_OK
from typing import Sized, Text
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
#sOverriding
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

#Screens
class PathScreen(Screen):
    pass
class LoadingScreen(Screen):
    pass
class WelcomeScreen(Screen):
    pass
class Organizer(ScreenManager):
    path_screen_obj = PathScreen()
    
    pass

#Builder
kv = Builder.load_file('new_window.kv')

#MainApp
class MyApp(App):
    def build(self):
        return kv

    def print_path(self, path):

        print(path)




if __name__ == '__main__':

    MyApp().run()
    # print(kivy.__version__) #You should use version 2.0.0



