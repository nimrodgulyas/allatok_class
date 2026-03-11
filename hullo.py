from allat import Allat

class Hullo(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "hullo", eletkor_, "szikla", "kicsi")

    def napozik(self):
        print(f"{self.nev} napozik a kövön.")
