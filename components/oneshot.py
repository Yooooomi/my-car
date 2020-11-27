import core
from component import Component
import asyncio

class Oneshot(Component):
    async def start(self):
        core.core.delete_component(self)
        await asyncio.sleep(5)
        print("End start")

    def stop(self):
        super().stop()
        print("Closed")