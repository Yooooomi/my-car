from component import Component

class TestSync(Component):
    async def start(self):
        print("I started")

    def stop(self):
        print("I stopped")