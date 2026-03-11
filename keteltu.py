from allat import Allat

class Madar(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "madar", eletkor_, "erdő", "kicsi")
    
    def csiripel(self):
        print(f"{self.nev} csiripel.")

class Keteltu(Allat):
    def __init__(self, nev_, eletkor_):
        super().__init__(nev_, "keteltu", eletkor_, "tópart", "kicsi")
    
    def brekeg(self):
        print(f"{self.nev} brekeg.")