import random

ZAČETEK = 'S'

ŽE_UGIBANO = 'D'
PRAVILNI_UGIB = 'C'
NEVELJAVEN_UGIB = 'N'

ZMAGA = 'W'

class Igra:
    def __init__(self, beseda, datoteka_besed, ugibi):
        self.beseda = beseda.lower()
        self.koncnica = beseda[-2:-1]
        self.datoteka_besed = datoteka_besed
        self.ugibi = ugibi

    def zmaga(self, ugib):
        with open(self.datoteka_besed, encoding="utf-8") as f:
            množica_besed = f.read().split("/n")
            for beseda in množica_besed:            
                if ugib[-2:-1] == beseda[ :1 ]:
                    return False
        
        return True

    def ugibaj(self, ugib):
        ugib = ugib.lower()

        if ugib in self.ugibi:
            return ŽE_UGIBANO

        with open(self.datoteka_besed, encoding="utf-8") as f:
            if ugib not in f:
                return NEVELJAVEN_UGIB
        
        self.ugibi.append(ugib)

        if ugib[0 : 1] == self.koncnica:
            if self.zmaga(ugib):
                return ZMAGA
            else:
                return PRAVILNI_UGIB

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
            igra = Igra(beseda, f)

        self.igre[id_igre] = (igra, ZAČETEK)
        return id_igre