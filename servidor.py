import socket
import sys

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al puerto
server_address = ('localhost', 5000)
print('Iniciando en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Escuchar por conexiones entrantes
sock.listen(1)

while True:
    # Esperar una conexión
    print('Esperando conexión.')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde: ', client_address)

        # Recibir los datos en pequeños fragmentos y retransmitirlos
        while True:
            data = connection.recv(16)
            print('Recibido {!r}'.format(data.decode('utf-8')))
            if data == b'DESCONEXION':
                break

            data = data.upper()

            if data == b'HOLA SERVIDOR':
                data = b'HOLA CLIENTE'
            
            connection.sendall(data)
                

    finally:
        # Cerrando conexión
        print('Cliente cierra la conexión con el servidor.')
        connection.close()