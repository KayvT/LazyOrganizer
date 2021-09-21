from os import W_OK
from typing import Sized, Text
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class Organizer(App):

    def build(self):
        # Build Components
        self.window = GridLayout()
        self.window.cols = 1



        ## Widgets
        self.initalGreetingLabel = Label(text="Hi there! What should I call you?")
        self.user_name = TextInput(multiline=False)
        self.enter_button = Button(text="Take me in!")

        self.enter_button.bind(on_press=self.proceed)

        self.window.add_widget(self.initalGreetingLabel)
        self.window.add_widget(Image(source="./assets/logo.png"))
        self.window.add_widget(self.user_name)
        self.window.add_widget(self.enter_button)
        

        return self.window

    def proceed(self, instance):
        self.initalGreetingLabel.text = "Hi, " + self.user_name.text + "!"

if __name__ == '__main__':
    Organizer().run()
    # print(kivy.__version__) #You should use version 2.0.0



