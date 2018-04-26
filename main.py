from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior


class HorizontalButton(ButtonBehavior, Widget):
    def __init__(self, **kwargs):
        super(HorizontalButton, self).__init__(**kwargs)


class VerticalButton(ButtonBehavior, Widget):
    def __init__(self, **kwargs):
        super(VerticalButton, self).__init__(**kwargs)
    pass


class CircleDisplay(Widget):
    pass


class DriveSession(Widget):
    def __init__(self):
        super(DriveSession, self).__init__()

    speedometer =  ObjectProperty(None)
    gas_pedal =  ObjectProperty(None)
    brake_pedal =  ObjectProperty(None)

    speed = NumericProperty(0)

    def brake(self):
        self.speed = self.speed * 0.85

    def accelerate(self):
        self.speed = self.speed * 1.1 + 1.0


class CarApp(App):
    def build(self):
        session = DriveSession()
        return session


if __name__ == "__main__":
    CarApp().run()


