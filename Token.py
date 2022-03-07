class Token:
    value = None

    def __init__(self, type):
        self.type = type
    
    def set_value(self, val):
        self.value=val