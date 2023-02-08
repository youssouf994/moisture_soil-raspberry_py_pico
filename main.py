from machine import ADC, Pin
import time

lettura_sensore=ADC(Pin(26))

def misura_sensore():
    min=0
    max=65535
    umidità=(max-lettura_sensore.read_u16())*100/(max-min)
    return umidità

while True:
    umidita_finale=misura_sensore()
    print("umidità percepita ", umidita_finale, " %")
    time.sleep(5)