#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime


def get_daten_fuers_kursheft(startdatum, enddatum, kurstage):
    wochentage = ["Montag", "Dienstag", "Mittwoch",
                  "Donnerstag", "Freitag", "Samstag",
                  "Sonntag"]
    datum = startdatum
    while datum <= enddatum:
        if wochentage[datum.weekday()] in kurstage:
            print(wochentage[datum.weekday()][:2],"., ",
                  datum.strftime('%d.%m.'), " ",
                  kurstage[wochentage[datum.weekday()]],
                  sep="")
        datum += datetime.timedelta(1)


def get_notenstufen(separator=";"):
    for note in range(1,7):
        for vorzeichen in ["+","","-"]:
            if note == 6:
                print(note)
                break
            else:
                print(str(note) + vorzeichen, end=";")
    

def klassenspiegel_erzeugen(eins,
                            zwei   = 0,
                            drei   = 0,
                            vier   = 0,
                            fuenf  = 0,
                            sechs  = 0,
                            anzahl = None):
    box = '''
Notenspiegel
============
    
+---+---+---+---+---+---+---+-----+---+
| n | 1 | 2 | 3 | 4 | 5 | 6 |  Ø  | N |
+---+---+---+---+---+---+---+-----+---+
| {:2d}| {:2d}| {:2d}| {:2d}| {:2d}| {:2d}| {:2d}| {:.2f}| {:2d}|
+---+---+---+---+---+---+---+-----+---+

n = Anzahl der Lernenden
N = Nachschrift
    '''
    n  = eins + zwei + drei + vier + fuenf + sechs
    schnitt = (eins + zwei * 2 + drei * 3 + vier * 4 + fuenf * 5 + sechs * 6) / n
    if anzahl is None:
        anzahl = 0
    else:
        anzahl -= n
    print(box.format(n, eins, zwei, drei, vier, fuenf, sechs, schnitt, anzahl))


def kursliste2schuelerliste(kursliste, nurklausur=False):
    """ Wandelt die Schülerdaten einer Kursliste
    in eine „Vornamen Nachnamen“-Liste um und
    gibt sie auf dem Bildschirm aus.
    
    Bekommt eine wohlgeformte Kursliste der
    folgenden Form als mehrzeiligen String:
        1. NACHNAME, VORNAME WEITERER_VORNAME GKS X

    Der Parameter nurklausur legt fest, ob nur
    die Schüler und Schülerinnen ausgegeben
    werden, die das Fach schriftlich gewählt 
    haben.
        
    Und liefert zurück:
        VORNAME WEITERER_VORNAME NACHNAME

    Bekannte Probleme: Verursacht Probleme,
    wenn der erste Vorname nicht der Haupt-Vorname
    ist und berücksichtigt "von" usw. nicht.
    """
    kursliste = kursliste.split("\n")
    ausgabe = []
    for namenszeile in kursliste:
        nachname, vorname = namenszeile.split(". ")[1].split(", ")
        vorname = vorname.split(" ")[0]
        if nurklausur == False:
            # Gib alles aus
            ausgabe.append(vorname + " " + nachname)
        elif nurklausur and namenszeile.endswith(" X"):
            # Gib die Klausurschreiberinnen
            # und Klausurschreiber aus
            ausgabe.append(vorname + " " + nachname)
    ausgabe_str = "\n".join(ausgabe)
    ausgabe_str = ausgabe_str.replace("  ", " ")
    for line in ausgabe_str.split("\n"):
        print(line)


def kursliste2schuelerliste2(kursliste, nurklausur=False):
    kursliste = kursliste.replace("AB3 X", "_KLAUSUR_").replace("AB4 X", "_KLAUSUR_").replace("GKS X", "_KLAUSUR_").replace("GKM", "")
    for line in kursliste.split("\n"):

        if nurklausur:
            if "_KLAUSUR_" in line:
                line = line.replace("_KLAUSUR_", "")
                nachname, vornamen = line.split(". ")[1].split(", ")
                print(vornamen.strip(" "), nachname.strip(" "))
        else:
            line = line.replace("_KLAUSUR_", "")
            nachname, vornamen = line.split(". ")[1].split(", ")
            print(vornamen.strip(" "), nachname.strip(" "))


def nachname_vorname2vorname_nachname(namensliste):
    # "Nachname, Vorname" --> "Vorname Nachname"
    namensliste = namensliste.split("\n")
    for line in namensliste:
        nachname, vorname = line.split(", ")
        print(vorname.strip(" "), nachname.strip(" "))
    

if __name__ == "__main__":

    """
    Test der Funktion get_daten_fuers_kursheft()
    ============================================

    Ausgabe aller Tage mit einer Veranstaltung in einem
    Kurs zwischen Start- und Enddatum zwecks Eintragung
    in einem Kursheft.
    """
    print("\n\nTest der Funktion get_daten_fuers_kursheft()")

    startdatum = datetime.date.today()
    enddatum   = datetime.date(2018,2,20)
    kurstage   = {"Montag"   : "ES",
                  "Mittwoch" : "DS"}
    get_daten_fuers_kursheft(startdatum, enddatum, kurstage)


    """
    Test der Funktion get_notenstufen()
    ===================================

    Man erhält eine Liste mit den Notenstufen.    
    """
    print("\n\nTest der Funktion get_notenstufen()")
    get_notenstufen(";")

    
    """
    Test der Funktion klassenspiegel_erzeugen()
    ===========================================

    Die Funktion erzeugt einen Klassenspiegel auf
    Basis der Eingaben und gibt unter N die Zahl der
    Nachschreiberinnen und Nachschreiber an.
    """
    print("\n\nTest der Funktion klassenspiegel_erzeugen()")

    klassenspiegel_erzeugen(1,2,3,3,2,1,12)


    """
    Test der Funktion kursliste2schuelerliste()
    ===========================================

    Die Funktion extrahiert aus der Namensliste einer
    Kursliste (PDF) Vor- und Nachname und gibt die Daten
    aus. Eingestellt werden kann durch Parameter-Übergabe,
    ob nur Klausurschreiberinnen und Klausurschreiber
    ausgegeben werden sollen.

    ID  Name       Vorname  Fach  Klausur
     1  Broderick  Matthew  AB3   X
    """
    print("\n\nTest der Funktion kursliste2schuelerliste()")

    kursliste = """1. Broderick, Matthew AB3 X
    2. Coleman, Dabney Wharton GKM
    3. Wood, John GKS X
    4. Sheedy, Alexandra Elizabeth GKM
    5. Corbin, Leonard Barry AB4 X"""
    kursliste2schuelerliste(kursliste, nurklausur=False)


    """
    Test der Funktion kursliste2schuelerliste2()
    ===========================================

    Wie zuvor, diese Funktion ist etwas robuster und
    hat weniger logische Probleme. Etwaige überzählige
    Vornamen sind von Hand zu entfernen.
    """
    print("\n\nTest der Funktion kursliste2schuelerliste2()")

    kursliste = """1. Broderick, Matthew von AB3 X
    2. Coleman, Dabney Wharton van GKM
    3. Wood, John GKS X
    4. Sheedy, Alexandra Elizabeth GKM
    5. Corbin, Leonard Barry AB4 X"""
    kursliste2schuelerliste2(kursliste, nurklausur=False)


    """
    Test der Funktion nachname_vorname2vorname_nachname()
    =====================================================
    
    Die Funktion erhält eine Liste der Form "Nachname,
    Vorname" und macht daraus "Vorname Nachname", wobei
    überzählige Vornamen von Hand zu löschen sind.
    """
    print("\n\nTest der Funktion nachname_vorname2vorname_nachname()")
    
    namensliste = """Broderick, Matthew
                     Coleman, Dabney
                     Wood, John
                     Sheedy, Ally
                     Corbin, Barry"""
    nachname_vorname2vorname_nachname(namensliste)
