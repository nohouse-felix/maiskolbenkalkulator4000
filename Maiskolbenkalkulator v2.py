# Willkommensnachricht
def welcome_message():
    print("Willkommen zum Maiskolbenkalkulator 4000!")
    print("Mithilfe dieses Programms kann der Ertrag eines Maisfelds berechnet werden.\n")
    start = input("Zum Fortfahren bitte die Enter-Taste drücken. ")


# Verabschiedungsnachricht
def goodbye_message():
    print("\nVielen Dank dass du den Maiskolbenkalkulator 4000 genutzt hast!")


# Fehlermeldung bei ungültiger Eingabe
def error_message():
    print("\nAuweia! Das hat leider nicht geklappt. Bitte wähle mittels Angabe der korrespondierenden Nummer eine Antwortmöglichkeit aus.\n")


# Dichte des Maisfelds bestimmen
def get_dichte():
    dichte_input = input("\nWie dicht stehen die Maiskolben am Feld aneinander?\n[1] Weniger dicht\n[2] Durchschnittlich\n[3] Dichter als normal\n[4] Sehr dicht\n")
    if dichte_input == "1":
        return 6
    elif dichte_input == "2":
        return 8
    elif dichte_input == "3":
        return 10
    elif dichte_input == "4":
        return 12
    else:
        error_message()
        return get_dichte()
    

# Kolben-Beschaffenheit der Pflanzen bestimmen
def get_kolben():
    kolben_input = input("\nWie viele Kolben trägt eine Pflanze im Durchschnitt? (1, 2 oder 3):\n")
    if kolben_input == "1":
        return 1
    elif kolben_input == "2":
        return 2
    elif kolben_input == "3":
        return 3
    else:
        error_message()
        return get_kolben()
    

# Fläche des Maisfelds bestimmen
def get_flaeche():
    # Auswahl der Angabe-Variante
    flaeche_input_type = input("\nWie groß ist das Maisfeld?\nWähle zwischen Angabe in:\n[1] Länge und Breite\n[2] Fläche in m²:\n")
    
    # Angabe in Länge und Breite
    if flaeche_input_type == "1":
        laenge = input("\nBitte gib die Länge des Maisfelds in Metern an: ")
        # Wenn die Länge kleiner oder gleich 0 ist, wird eine Fehlermeldung ausgegeben und der Vorgang wiederholt.
        if float(laenge) <= 0:
            print("\nUngültige Eingabe. Bitte versuche es erneut.")
            return get_flaeche()
        # Wenn die Länge größer oder gleich 1 ist, wird der Vorgang fortgesetzt und die Breite abgefragt.
        elif float(laenge) >= 1:
            breite = input("\nBitte gib die Breite des Maisfelds in Metern an: ")
            # Wenn die Breite kleiner oder gleich 0 ist, wird eine Fehlermeldung ausgegeben und der Vorgang wiederholt.
            if float(breite) <= 0:
                print("\nUngültige Eingabe. Bitte versuche es erneut.")
                return get_flaeche()
            # Wenn die Breite größer oder gleich 1 ist, wird die Fläche berechnet und ausgegeben.
            elif float(breite) >= 1:
                flaeche = float(laenge) * float(breite)
                return flaeche
            else:
                error_message()
                return get_flaeche()
        else:
            print("\nUngültige Eingabe. Bitte versuche es erneut.")
            return get_flaeche()
    
    # Angabe in Quadratmetern
    elif flaeche_input_type == "2":
        flaeche = input("\nÜber wie viele Quadratmeter streckt sich das Maisfeld? ")
        # Wenn die Fläche kleiner oder gleich 0 ist, wird eine Fehlermeldung ausgegeben und der Vorgang wiederholt.
        if float(flaeche) <= 0:
            print("\nUngültige Eingabe. Bitte versuche es erneut.")
            return get_flaeche()
        # Wenn die Fläche größer oder gleich 1 ist, wird die Fläche ausgegeben.
        elif float(flaeche) >= 1:
            return float(flaeche)
        # Sollten die ersten beiden Möglichkeiten nicht zutreffen, wird eine Fehlermeldung ausgegeben und der Vorgang wiederholt.
        else:
            print("\nUngültige Eingabe. Bitte versuche es erneut.")
            return get_flaeche()

    # Sollte keine gültige Auswahl getroffen worden sein, wird eine Fehlermeldung ausgegeben und der Vorgang wiederholt.    
    else:
        error_message()
        return get_flaeche()


# Maiskolbenkalkulator
def maiskolben_kalkulator():
    welcome_message()
    dichte = get_dichte()
    kolben = get_kolben()
    flaeche = get_flaeche()
    ertrag = dichte * kolben * flaeche

    print("\nBei einer Dichte von", dichte, "Maispflanzen pro Quadratmeter, einer Kolbenbeschaffenheit von", kolben, "Maiskolben pro Pflanze und einer Fläche von", round(flaeche, 2), "m² ergibt sich ein Ertrag von", round(ertrag), "Maiskolben.")
    goodbye_message()


maiskolben_kalkulator()