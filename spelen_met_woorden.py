import random

# Print het aantaal woorden in een lijst met woorden
def print_aantal_woorden(woordenlijst):
    aantaal_woorden = len(woordenlijst)
    print(f'Er staan {aantaal_woorden} woorden op je lijst.')

# Print alle woorden met het grootste aantaal letters
def print_langste_woorden(woordenlijst):
    max_letters = 0
    woorden = []
    for woord in woordenlijst:
        if len(woord) > max_letters:
            woorden = [woord]
            max_letters = len(woord)
        elif len(woord) == max_letters:
            woorden.append(woord)
    if len(woorden) == 1:
        print('Het langste woord in je lijst is', woorden[0])
    else:
        print('De langste woorden in je lijst zijn:')
        for woord in woorden:
            print(woord)

# Keert de string om: ABC -> CBA
def keer_string_om(str):
    kopiestr = ""
    for letter in str:
        kopiestr = letter + kopiestr

    return kopiestr

# Controleer of een woord een palindroom is
def is_palindroom(a):
    if a == keer_string_om(a):
        return True
    else:
        return False

# Print alle palindromen
def print_palindromen(woordenlijst):
    print('Je palindromen zijn:')
    for woord in woordenlijst:
        if is_palindroom(woord):
            print(woord)

# Print alle woorden die 'omgekeerd' ook voorkomen in de lijst
def print_omkeerbaar(woordenlijst):
    # maak een lijst van alle omgekeerde woorden
    woordenlijst_omgekeerd = [keer_string_om(woord) for woord in woordenlijst]
    # check welke woorden zowel in de orspronkelijke als de 
    # omgekeerde lijst voorkomen
    omkeerbaar = set(woordenlijst_omgekeerd).intersection(set(woordenlijst))
    print('Dit zijn alle woorden die ook omgekeerd in je lijst voorkomen:')
    for woord in omkeerbaar:
        print(woord)

# Check of een ingevoerd woord voorkomt in de lijst, of als 
# onderdeel van woorden. Print alle deze woorden
def vind_woorden_met(woordenlijst):
    invoer = input('Welk woord wil je zoeken?: ')
    if invoer == '':
        print("Tsts. Alle woorden inhouden een lege string")
    else:
        print(f'Dit zijn alle woorden in de lijst die {invoer} inhouden:')
        for woord in woordenlijst:
            if invoer in woord:
                print(woord)

# Check of a een anagram is van b
def zijn_anagrammen(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    return a == b


# Print alle woorden die je kunt maken van de letters van een 
# ingevoerd string
def print_anagrammen(woordenlijst):
    invoer = input('Van wel woord wil je de anagrammen vinden?: ')
    anagrammen = []
    for woord in woordenlijst:
        if zijn_anagrammen(woord, invoer):
            anagrammen.append(woord)
    if len(anagrammen) == 0:
        print('Sorry, ik kon geen anagrammen vinden')
    else:
        print('Dit zijn de anagrammen van je woord: ')
        for anagram in anagrammen:
            print(anagram)

def argmax(lijst):
    return lijst.index(max(lijst))

# Splitst een woord in een lijst van lettergrepen
def lettergrepen(woord, woordenlijst):
    # Als het een samengesteld woord is
    deelwoorden_tupel = deelwoorden(woord, woordenlijst)
    print('deelworden:', deelwoorden_tupel)
    lettergrepen_lijst = []
    for deelwoord in deelwoorden_tupel:
        lettergrepen_lijst.extend(splits_deelwoord(deelwoord))
    print(lettergrepen_lijst)

# Vind alle deelwoorden van een samengesteld woord
def deelwoorden(woord, woordenlijst):
    # Maak een lijst van alle mogelijke deelwoorden. (Ze moeten langer dan 4 letters zijn, 
    # anders krijg je te veel nonsensical matches)
    lange_woorden = get_lange_woorden(5, woordenlijst)
    # Maak een lijst van woorden die aan het eind van het gegeven woord voorkomen
    kandidaten = []
    for lijst_woord in lange_woorden:
        if woord.endswith(lijst_woord):
            kandidaten.append(lijst_woord)
    # probeer het woord zonder 's' aan het eind
    if len(kandidaten) == 0 and woord.endswith('s'):
        deelwoorden_met_s = deelwoorden(woord[:-1], woordenlijst)
        deelwoorden_met_s[-1] += 's'
        return deelwoorden_met_s
    # Als alleen het orspronkelijke woord in de kandidatenlijst voorkomt geef het onveranderd terug
    if (len(kandidaten) == 1 and kandidaten[0] == woord) or len(kandidaten) == 0:
        return [woord]
    # Neem het langste woord uit de kandidatenlijst en splits darop
    # Splits de gevondene deelwoorden recursief in kleinere deelwoorden
    else:
        if woord in kandidaten:
            kandidaten.remove(woord)
        langste_woord =  max(kandidaten, key=len)
        deel_1 = deelwoorden(woord[:-len(langste_woord)], woordenlijst)
        deel_2 = deelwoorden(langste_woord, woordenlijst)
        return deel_1 + deel_2

# Splits een niet-samengesteld woord in lettergrepen
def splits_deelwoord(woord):
    lettergrepen_lijst = []
    eind_laatste_lettergreep = 0
    # Vind alle groepen van op elkaar volgende klinkers
    for i, letter in enumerate(woord):
        # als de letter aan het eind van een klinkergroep staat
        if i!=len(woord)-1 and is_klinker(letter) and not is_klinker(woord[i+1]):
            # vind volgende klinkergroep
            klinkergroep_gevonden = False
            j = i+1
            while not klinkergroep_gevonden and j<len(woord)-1:
                j += 1
                if is_klinker(woord[j]):
                    klinkergroep_gevonden = True

            aantaal_medeklinkers = j-i-1
            # als we aan het woordeinde zijn
            if not klinkergroep_gevonden:
                # pak alle overige letters in de laatste lettergreep
                eind_nieuwe_lettergreep = len(woord)
            # als er 1 medeklinker tussen 2 klinkergroepen zit
            elif aantaal_medeklinkers == 1:
                # split voor de medeklinker
                eind_nieuwe_lettergreep = i+1
            # uitzondering: 'sch' word niet gesplitst
            elif 'sch' in woord[i+1:j]:
                # splits voor 'sch'
                eind_nieuwe_lettergreep = woord.index('sch')
            # als er 2 of meer medeklinkers tussen 2 klinkergroepen zitten
            elif aantaal_medeklinkers >= 2:
                # split tussen de 2 medeklinkers
                eind_nieuwe_lettergreep = i+2
            lettergrepen_lijst.append(woord[eind_laatste_lettergreep:eind_nieuwe_lettergreep])
            eind_laatste_lettergreep = eind_nieuwe_lettergreep
        
    if is_klinker(woord[-1]):
        lettergrepen_lijst.append(woord[eind_laatste_lettergreep:])

    return lettergrepen_lijst

def is_klinker(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


# Check of a en b rijmen
def rijmen(a, b):
    pass

# Print alle woorden uit de lijst die rijmen op een ingevoerd woord
def print_rijmen(woordenlijst):
    invoer = input('Op welk woord zal ik je rijmen vinden?: ')
    while not invoer.isalpha():
        invoer = input('Je hebt geen woord ingetypt. Probeer het nog een keer: ')
    print('''Leuk dat je een woord hebt ingetypt. Checken of twee woorden rijmen is helaas
    heel erg ingewikkeld. Daarom moet je je rijmen zelf verzinnen''')
        
# Geeft een lijst van alle woorden in de woordenlijst die minstens aantaal_letters letters lang zijn
def get_lange_woorden(aantaal_letters, woordenlijst):
    return [woord for woord in woordenlijst if len(woord)>=aantaal_letters]

def raadspel(woordenlijst):
    invoer = input('''-------------------------------------------------
    Welkom bij mijn raadspel. Ik ga een woord verzinnen en jij moet het raden.
    Als je het woord weet mag je het intypen en enter drukken. Als je geen 
    woord intypt en op enter drukt geef ik je nieuwe letters om het raden 
    makkelijker te maken. 
    Hoe veel letters moet mijn woord minimal hebben?: ''')
    while not invoer.isnumeric():
        invoer = input('Voer alsjeblieft een integer tussen 1 en 46 in: ')
    # maak een lijst van alle woorden die lang genoeg zijn
    lange_woorden = get_lange_woorden(int(invoer), woordenlijst)
    # kies toevallig een woord
    oplossing = lange_woorden[random.randint(0, len(lange_woorden))]
    
    letter_lijst = list(set(oplossing))
    letter_lijst.sort()
    string = '_ ' * len(oplossing)
    for i, letter in enumerate(letter_lijst):
        for j, letter_op in enumerate(oplossing):
            if letter == letter_op:
                string = string[:j*2] + letter_op + string[j*2+1:]
        invoer = input(f'{string}: ')
        if i == len(letter_lijst)-1:
            print('Hoera, mijn woord was zo moeilijk dat je het niet hebt kunnen raden')
        elif invoer == '':
            continue
        elif invoer == oplossing:
            print('Gefeliciteerd! Je hebt het woord geraden.')
            break
        else: 
            print('Dit was niet het woord wat ik bedacht had. Ik geef je nog een letter. ')
    
    


with open('woorden.txt', 'rt') as bestand_met_woorden:
    lijst_met_woorden = bestand_met_woorden.readlines()
    # Strip alle newlines aan het woordeinde
    lijst_met_woorden = [woord.rstrip() for woord in lijst_met_woorden]
    

#print_aantal_woorden(lijst_met_woorden)
#print_langste_woorden(lijst_met_woorden)
#print_palindromen(lijst_met_woorden)
#print_omkeerbaar(lijst_met_woorden)
#vind_woorden_met(lijst_met_woorden)
#print_anagrammen(lijst_met_woorden)
#print_rijmen(lijst_met_woorden)
#raadspel(lijst_met_woorden)
#lettergrepen('moeten', lijst_met_woorden)
#lettergrepen('venster', lijst_met_woorden)
#lettergrepen('enclave', lijst_met_woorden)
#lettergrepen('obstinaat', lijst_met_woorden)
#lettergrepen('geschiedenis', lijst_met_woorden)
#lettergrepen('autobandventieldopjesfabriek', lijst_met_woorden)
#lettergrepen('waarom',lijst_met_woorden)
#lettergrepen('kitesurfen', lijst_met_woorden)
#lettergrepen('intimideren', lijst_met_woorden)
lettergrepen('arbeidsongeschiktheidsverzekeringsmaatschappij', lijst_met_woorden)
