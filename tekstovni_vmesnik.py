import model

def izpis_poraza(igra):
    return f"Žal si izgubil. Več sreče prihodnjič!"

def izpis_zmage(igra):
    return f"Čestitke, uspelo ti je!"

def izpis_igre(igra):
    besedilo = f""" beseda: {igra.beseda_1()}"""
    return besedilo

def zahtevaj_vnos():
    vnos = input("Ugibaj: ")
    
    if len(vnos) == 1:
        return vnos
    else:
        return None

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