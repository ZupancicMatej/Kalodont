import random

class Kalodont:
    def __init__(self, datoteka_besed):
        self.igre = {}
        self.datoteka_besed = datoteka_besed

    def prost_id_igre(self):
        if self.igre.keys():
            return max(self.igre.keys()) + 1
        else: 
            return 0

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        with open(self.datoteka_besed, encoding="utf-8") as f:
            množica_besed = f.read().split("/n")


        beseda = random.choice(množica_besed)
        
        igra = Igra(beseda)

        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre