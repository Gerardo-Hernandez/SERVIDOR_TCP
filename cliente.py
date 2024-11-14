import socket
import sys

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 5000)
print('Conectado a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    while True:
        # Enviando mensaje
        message = input('Cliente envía:').encode('utf-8')
        sock.sendall(message)
        
        data = sock.recv(16).decode('utf-8')
        if message == b'DESCONEXION':
            break
        print('Servidor responde {!r}'.format(data))
        
finally:
    # Cerrando conexión
    print('Servidor cierra la conexión con el cliente.')
    sock.close()