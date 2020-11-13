import pickle

# Het programma begint met een basisset aan dieren
# De gebruikte datastructuur is een Python dictionary

default_dieren = {
    'vraag': 'heeft het dier 4 poten',
    'nee': {
        'vraag': 'knruipt het op bladeren',
        'ja':'rups',
        'nee':'huismus'
    },
    'ja': 'olifant'
}

# Herhalen zolang de gebruiker dat wil
def raad_het_dier():
    dieren = laad_boomstructuur()
    print('Neem een dier in gedachten...')
    prompt = 'Ben je er klaar voor?'
    while vraag_ja_nee(prompt):
        doorloop_dieren_boomstructuur(dieren)
        prompt = 'Wil je nog een keer spelen?'
    bewaar_boomstructuur(dieren)


# Laad opgeslagen boomstructuur uit een pickle file
def laad_boomstructuur():
    if vraag_ja_nee('Wil je een opgeslagen spel laden?'):
        try:
            with open('dieren_boomstructuur.pickle', 'rb') as bestand:
                dieren = pickle.load(bestand)
        except:
            print('Sorry, ik kon geen opgeslagen spel laden. Laten we een nieuwe beginnen.')
            dieren = default_dieren
    else:
        dieren = default_dieren
    return dieren


# Sla de boomstructuur in een pickle file op
def bewaar_boomstructuur(dieren):
    with open('dieren_boomstructuur.pickle', 'wb') as bestand:
        pickle.dump(dieren, bestand)

# Doorloop een tak
def doorloop_dieren_boomstructuur(tak):
    # We stellen eerst de vraag die op de tak beschikbaar is
    # De vraag heeft het formaat ['is'|'heeft'] het dier 'eigenschap'
    richting = vraag_ja_nee(tak['vraag'].capitalize() + '?')
    nieuwe_tak = lagere_tak(tak, richting)

    if dier_gevonden(nieuwe_tak):
        eindig_spel(nieuwe_tak, tak, richting)
    else:
        doorloop_dieren_boomstructuur(nieuwe_tak)

# Een dier is gevonden als de tak waarop we zitten eindigt in een blad,
# in plaats van in een lagere tak. Een blad is een string, een
# lagere tak is een dict. We controleren op een blad met de functie
# isinstance
def dier_gevonden(tak):
    is_blad = not isinstance(tak, dict)
    return is_blad

def eindig_spel(blad, stam, richting):
    if vraag_ja_nee('Is je dier misschien een ' + blad + '?'):
        print('Yes! Ik het het geraden! Ik ben zo goed!')
    else:
        bewaar_nieuw_dier(stam, welke_kant(richting), blad)

def bewaar_nieuw_dier(hogere_tak, kant, oud_dier):
    nieuw_dier = input('Oh, wat jammer dat ik het niet heb geraden! Welk dier zat je aan te denken? ')
    if nieuw_dier.startswith('een '):
        nieuw_dier = nieuw_dier[4:len(nieuw_dier)]
    nieuwe_vraag = input('En welke vraag had ik moeten stellen om onderscheid te maken tussen een ' + oud_dier.lower() + ' en een ' + nieuw_dier.lower() + '? ')
    vraag_met_nieuw_dier = nieuwe_vraag.replace('het', 'een '+nieuw_dier)
    antwoord_nieuw_dier = vraag_ja_nee(f'Een wat is het antwoord op de vraag "{vraag_met_nieuw_dier.capitalize()}?"')
    hogere_tak[kant] = {
        'vraag': nieuwe_vraag.lower().rstrip('? ').lstrip(' ').replace('  ', ' '),
        bool_to_ja_nee(antwoord_nieuw_dier): nieuw_dier.lower(),
        bool_to_ja_nee(not antwoord_nieuw_dier): oud_dier
    }

# Geef een deel van de boomstructuur terug die begint met
# ja of nee
def lagere_tak(tak, richting):
    if richting:
        return tak['ja']
    else:
        return tak['nee']

def welke_kant(ja):
    if ja:
        return 'ja'
    else:
        return 'nee'

def vraag_ja_nee(vraag):
    antwoord = input(vraag + ' ')
    return is_ja(antwoord)

def is_ja(tekst):
    if tekst.lower().startswith('j'):
        return True
    else:
        return False

def bool_to_ja_nee(bool):
    if bool:
        return 'ja'
    else:
        return 'nee'

raad_het_dier()
