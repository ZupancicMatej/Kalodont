import model

def izpis_poraza(igra):
    return f"Žal si izgubil. Več sreče prihodnjič!"

def izpis_zmage(igra):
    return f"Čestitke, uspelo ti je!"

def izpis_igre(igra):
    besedilo = f""" beseda: {igra.beseda}"""
    return besedilo



def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))

        crka = zahtevaj_vnos()
        while crka is None:
            #print ("Napačen vnos!")
            crka = zahtevaj_vnos()

        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()