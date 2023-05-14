from wifi_lib import conecta
import urequests

print("Conectando...")
station = conecta("nomeRede", "senhaRede")
if not station.isconnected():
    print("Erro de conexão!!")
else:
    print("Conectado")