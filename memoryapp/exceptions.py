class NotFoundException(Exception):
    def __init__(self, item):
        self.item = item
