from os import W_OK, listdir, path, makedirs
from pathlib import Path
from os.path import isfile, join
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
import shutil
#sOverriding
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
#VARS
EXTENSION_DICT = dirs = {
    # Images
    ".jpeg": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".tiff": "Images",
    ".gif": "Images",
    ".ai": "Images",
    ".psd": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".webm": "Videos",
    ".flv": "Videos",

    # Music
    ".mp3": "Music",
    ".ogg": "Music",
    ".wav": "Music",
    ".flac": "Music",

    # Programs
    ".py": "Program Files",
    ".js": "Program Files",
    ".cpp": "Program Files",
    ".html": "Program Files",
    ".css": "Program Files",
    ".c": "Program Files",
    ".sh": "Program Files",
    ".exe": "Program Files",
    ".json": "Program Files",

    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".ods": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents"
}
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
        self.files_to_be_moved = [f'{path}\{file_}' for file_ in listdir(path) if isfile(f'{path}\{file_}')]
        print(len(self.files_to_be_moved))
        for file in self.files_to_be_moved:
            print(file)
            suffix = Path(file).suffix
            folder_name = EXTENSION_DICT[suffix]
            all_files = listdir(path)
            if folder_name in all_files:
                print("exists:", file)
                shutil.move(file, f'{path}\{folder_name}')
            else:
                print("does not exist: ", file)
                path_to = f'{path}\{folder_name}'
                makedirs(path_to)
                shutil.move(file, path_to)
                
        # print(self.files)

if __name__ == '__main__':

    MyApp().run()
    # print(kivy.__version__) #You should use version 2.0.0



