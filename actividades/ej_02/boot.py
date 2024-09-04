# Configuracion inicial
import network

# Configuracion de la red
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Cooperadora Alumnos', '')

print('Conectando a la red...')
while not sta_if.isconnected():
    pass

print('Conectado a la red')
print(sta_if.ifconfig())

