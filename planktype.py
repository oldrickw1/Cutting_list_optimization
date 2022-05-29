class PlankType:
    def __init__(self, name, length, value):
        self.name = name
        self.length = length
        self.value = value
        self.quality = int(name[0])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.length},{self.value})"
