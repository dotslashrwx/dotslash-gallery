from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import os

PHOTO_FOLDER = "/sdcard/DCIM/Camera"

class Gallery(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        photos = os.listdir(PHOTO_FOLDER)

        if photos:
            img = Image(source=os.path.join(PHOTO_FOLDER, photos[0]))
            self.add_widget(img)

class FocusGallery(App):
    def build(self):
        return Gallery()

FocusGallery().run()
