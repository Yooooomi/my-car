import asyncio
from typing import TypeVar

T = TypeVar("T")

class Core:
    def __init__(self):
        self.components = {}
        self.tasks = []
        self.loop = asyncio.get_event_loop()
        self.loop.set_exception_handler(lambda loop, dict : print(dict["exception"]))

    def wait(self) -> None:
        self.loop.run_forever()            

    def stop_if_not_cancelled(self, component):
        if not component.task.cancelled:
            self.delete_component(component)

    def add_component(self, component) -> None:
        key = type(component)
        if not key in self.components:
            self.components[key] = []
        self.components[type(component)].append(component)
        task = self.loop.create_task(component.start())
        component.assign_task(task)
        task.add_done_callback(lambda a : self.stop_if_not_cancelled(component))

    def get_component(self, typ: T, idx = 0) -> T:
        if not typ in self.components:
            return None
        value = self.components[typ]
        if idx >= len(value):
            return None
        return value[idx]
    
    def get_components(self, typ: T) -> T:
        if not typ in self.components:
            return None
        return self.components

    def delete_component(self, component) -> bool:
        key = type(component)
        if not key in self.components:
            return False
        value = self.components[key]
        old_length = len(value)
        component.stop()
        value.remove(component)
        return old_length != len(value)

    def delete_type(self, typ) -> bool:
        if not typ in self.components:
            return False
        value = self.components[typ]
        for i in value:
            i.stop()
        del self.components[typ]
        return True

core: Core = None
