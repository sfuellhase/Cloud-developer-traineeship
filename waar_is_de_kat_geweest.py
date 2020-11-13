import random

# initialisatie
aantal_dozen = 5
doos_met_kat = random.randint(0, aantal_dozen)
kat_gevonden = False
aantal_pogingen = 0

# Zoek de kat
while not kat_gevonden:
    aantal_pogingen += 1
    # Vraag gebruiker 
    invoer = input('In welke doos zoek je de kat?: ')
    while not invoer.isnumeric() or int(invoer)>aantal_dozen or int(invoer)<1:
        invoer = input(f'Voer alsjeblieft een integer tussen 1 en {aantal_dozen} in: ')
    # als doos_te_open gelijk aan doos_met_kat
    if int(invoer) == doos_met_kat:
        print(f'Je hebt de kat in {aantal_pogingen} pogingen gevonden.')
        kat_gevonden = True
    else:
        print('Kat niet gevonden. Probeer het nog een keer.')

    # verplaats de kat
    if doos_met_kat == 0:
        doos_met_kat += 1
    elif doos_met_kat == aantal_dozen-1:
        doos_met_kat -= 1
    else:
        doos_met_kat += random.choice([-1, 1])
