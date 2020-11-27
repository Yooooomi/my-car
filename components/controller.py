from component import Component
import asyncio
import xbox360controller
from xbox360controller import Xbox360Controller

class Controller(Component):
    def __init__(self):
        self.buttons = {}
        self.axis = {}
        self.controller = None

    def on_button_pressed(self, button):
        print(button)
        self.buttons[button.name] = True

    def on_button_released(self, button):
        self.buttons[button.name] = True

    def on_axis_moved(self, axis):
        if type(axis) == xbox360controller.controller.Axis:
            self.axis[axis.name] = [axis.x, axis.y]
        else:
            self.axis[axis.name] = axis.value

    def get_axis(self, axis):
        return self.axis.get(axis, 0)

    def get_button(self, button):
        return self.buttons.get(button, False)

    def connect(self):
        self.controller = Xbox360Controller()

        print("Controller connected")

        for button in controller.buttons:
            button.when_pressed = self.on_button_pressed
            button.when_released = self.on_button_released

        for axis in controller.axes:
            axis.when_moved = self.on_axis_moved

    async def start(self):
        while True:
            try:
                self.connect()
                while True:
                    self.controller.get_available()
                    await asyncio.sleep(5)
            except Exception as e:
                pass
            await asyncio.sleep(5)
