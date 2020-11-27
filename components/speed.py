import core
import asyncio
from components import controller

class Speed(Component):
    async def start(self):
        controller = core.core.get_component(controller.Controller)
        while True:
            await asyncio.sleep(0.1)
            x = controller.get_axis("LEFT-X")
            controller.get_button('RIGHT_ARROW')
            
