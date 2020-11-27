import asyncio
from component import Component
import core
from components import printer

unique = 0

class TestAsync(Component):
    async def start(self):
        self.printer = core.core.get_component(printer.Printer)

        global unique
        unique += 1
        self.unique = unique
        i = 0
        if unique == 3:
            raise "hello"
        while True:
            await asyncio.sleep(1)
            self.printer.print(self.unique)
            i += 1
            if i == 2:
                core.core.add_component(TestAsync())
