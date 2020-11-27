
class Component():
    def __init__(self):
        pass

    def assign_task(self, task):
        self.task = task

    async def start(self):
        pass

    def stop(self):
        self.task.cancel()
        pass
