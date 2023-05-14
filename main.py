#Gustavo Rudolfo Fernandes Corrêa
#Juliane Lael Bueno de Paulo 

import time
import urequests
import wifi
import dht
import machine
#Define o pino do sensor
PIN = 4
# Configura o objeto DHT e o Relé
d = dht.DHT11(machine.Pin(PIN))
r = machine.Pin(2, machine.Pin.OUT)
r.value(1)
# Loop infinito de leitura de temperatura e umidade
while True:
    # Imprime os dados no console
    d.measure()
    print("_____________________________________________________________________")
    print("")
    print("")
    print('Temperatura: {}°C, Umidade: {}%'.format(d.temperature(), d.humidity()))
    print("")
    if d.temperature() > 31 or d.humidity() > 70:
        r.value(0)
    else:
        r.value(1)
    # Envia os dados para o ThingSpeak
    response = urequests.get("https://api.thingspeak.com/update?apikey=&field1={}&field2={}".format(d.temperature(),d.humidity()))
    print("Enviando dados para o ThingSpeak...")
    if response.text == "0":
        print("")
        print("Erro ao enviar os dados para o ThingSpeak!")
        print("")
    else:
        print("")
        print("Dados enviados com sucesso!")
        print("")
        # Aguarda 15 segundos antes da próxima leitura devido as limitações de usuario gratis no ThingSpeak
    time.sleep(15)
