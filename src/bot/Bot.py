import importlib


class Bot:
    def __init__(self, options):
        self.e = importlib.import_module('engine.%(engine)s' % vars(options))

    def answer(self, q):
        return self.e.ask(q)
