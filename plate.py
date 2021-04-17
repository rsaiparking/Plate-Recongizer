import json

class Plate_Number:
    def __init__(self, number):
        self.plateNumber = number
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)