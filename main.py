import asyncio
import core
from components import test_async, test_sync, printer, controller, oneshot

def main():
    c = core.Core()
    core.core = c
    c.add_component(controller.Controller())
    c.add_component(oneshot.Oneshot())
    # c.add_component(printer.Printer())
    # c.add_component(test_sync.TestSync())
    # c.add_component(test_async.TestAsync())
    # c.add_component(test_async.TestAsync())
    c.wait()

if __name__ == "__main__":
    main()