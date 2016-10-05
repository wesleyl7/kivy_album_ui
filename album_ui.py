'''
Album UI with animated image buttons
=====================================

This example demonstrates creating and applying a zooming in/out animation to
a button widget with image. You should see a button with transparent text label 
 that will zoom with an animation when clicked.
'''

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.core.window import Window

class ImageButtonView(Button):
    def __init__(self, **kwargs):
        super(ImageButtonView, self).__init__(**kwargs)

    def set_title(self, title):
        self.ids.button_title.text = title
        self.ids.button_title.font_size = 14 
        
class ImageButtonLayout(RelativeLayout):
    def __init__(self, **kwargs):
        super(ImageButtonLayout, self).__init__(**kwargs)

        self.image_path = kwargs['path']
        self.image_name = kwargs['name']
        self.selected = False
        
        self.button = ImageButtonView(pos=(40, 30), size_hint=(0.8, 0.8), on_press=self.animate_up)
        self.button.set_title(self.image_name)
        self.button.background_normal = self.image_path
        self.add_widget(self.button)

    def animate_up(self, instance):
        self.parent.clear_selected_button()
        animate = Animation(pos=(0, 0), size_hint=(1.0, 1.0))
        animate.start(self.button)
        self.selected = True
        
    def animate_down(self):
        animate = Animation(pos=(40, 30), size_hint=(0.8, 0.8))
        animate.start(self.button)
        self.selected = False

    def get_animate_state(self):
        return self.selected

class ImageButtonGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ImageButtonGridLayout, self).__init__(**kwargs)

        self.rows = 2
        self.cols = 2
        self.button_selected = 0
        self.image_buttons = []
        image_array = ['Apple', 'Banana', 'Cantaloupe', 'Grapefruit']
        image_files = ['./Apple.jpg', './Banana.jpg', './Cantaloupe.jpg', './Grapefruit.jpg']
        self.image_count = len(image_array)

        for i in range(self.image_count):
            buttonView = ImageButtonLayout(size_hint = (0.4, 0.4), name=image_array[i], path=image_files[i])
            self.image_buttons.append(buttonView)
            self.add_widget(self.image_buttons[i])

    def clear_selected_button(self):
        for i in range(self.image_count):
            buttonView = self.image_buttons[i]
            if buttonView.get_animate_state() == True:
                buttonView.animate_down()

class Album_UIApp(App):

    def build(self):
        screen_view = ImageButtonGridLayout(size=Window.size)
        return screen_view

if __name__ == '__main__':
    Album_UIApp().run()
