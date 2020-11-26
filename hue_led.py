import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RUNNING = True
green = 27
red = 17
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)


# Berekend een rgb waarde van de gegeven hue waarde
def hue_to_rgb_led(h):
    if h < 1/3:
        r = 2 - h*6
        g = h * 6
        b = 0
    elif h < 2/3:
        r = 0
        g = 4 - h*6
        b = h*6 - 2
    else:
        r = h*6 - 4
        g = 0
        b = (1-h) * 6
    if r > 1:
        r = 1
    if g > 1:
        g = 1
    if b > 1:
        b = 1
    return (r*100, g*100, b*100)

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def isvalid(hue):
    if isfloat(hue) and float(hue)<=1 and float(hue)>=0:
        return True
    if hue.isnumeric() and int(hue) > 1 and int(hue)<=255:
        return True
    return False

def scale_to_float(hue):
    hue = float(hue)
    if hue <= 1:
        return hue
    return hue/255 

def query_user():
    hue = input('Beste gebruiker, voer een hue waarde in alsjeblieft.\
        Dat is of een float tussen 0 en 1 of een int tussen 0 en 255: ')
    while not isvalid(hue):
        hue = input('Dit was geen zinvol invoer. Probeer het nog een keer:')
    hue = scale_to_float(hue)
    return hue

def een_kleur():
    hue = query_user()
    (r, g, b) = hue_to_rgb_led(hue)
    try:
        while True:
            RED.start(r/2.55)
            GREEN.start(g/2.55)
            BLUE.start(b/2.55)
        
    except KeyboardInterrupt:
        # Gracefully exit the RGB lighting loop in order to shut down the lights
        GPIO.cleanup()

def alle_kleuren():
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    for hue in range(256):
        hue = scale_to_float(hue)
        (r, g, b) = hue_to_rgb_led(hue)
        print(hue, r, g, b)
        RED.ChangeDutyCycle(r)
        GREEN.ChangeDutyCycle(g)
        BLUE.ChangeDutyCycle(b)
        time.sleep(0.025)

alle_kleuren()
een_kleur()
