class BaseException(Exception):
    def __init__(self, e):
        self.message = e