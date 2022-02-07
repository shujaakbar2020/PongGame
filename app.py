from time import sleep
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongPaddle(Widget):
    pass


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self, dt):
        # moving the ball by using move() and other stuff
        self.ball.move()

        #bounce of top and bottom
        if (self.ball.y < 0) or (self.ball.y>self.height-50):
            self.ball.velocity_y *= -1
        #bounce of left and right
        if (self.ball.x < 0) or (self.ball.x>self.width-50):
            self.ball.velocity_x *= -1
    
    def on_touch_move(self, touch):
        if touch.x < self.width/ 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


PongApp().run()