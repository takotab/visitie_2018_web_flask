import json


class Praktijk(object):
    def __init__(self, temp=True):
        if temp:
            self.lst = json.load(open("praktijken.json"))["temp"]
        else:
            self.lst = json.load(open("praktijken.json"))["real"]
        self.dct = {str(i): item for i, item in enumerate(self.lst)}

    def get_tuple(self):
        return [(str(i), item) for i, item in enumerate(self.lst)]
