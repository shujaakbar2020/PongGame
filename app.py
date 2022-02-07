from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, RefrenceListProperty
from kivy.vector import Vector


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = RefrenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


PongApp().run()