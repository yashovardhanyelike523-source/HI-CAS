class Consumption:
    def __init__(self, name, used):
        self.name = name
        self.used = used

    def to_dict(self):
        return {"name": self.name, "used": self.used}