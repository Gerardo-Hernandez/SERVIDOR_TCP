# SERVIDOR_TCP

Este proyecto implementa un servidor TCP en Python.

## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Gerardo-Hernandez/SERVIDOR_TCP.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd SERVIDOR_TCP
    ```

## Uso

### Servidor

Para iniciar el servidor, ejecuta el siguiente comando:

```bash
python servidor.py
```

El servidor escuchará en localhost en el puerto 5000.

### Cliente

Para iniciar el cliente, ejecuta el siguiente comando:

```bash
python cliente.py
```

El cliente se conectará al servidor en localhost en el puerto 5000.

## Ejemplo de Comunicación

1. Inicia el servidor.
2. Inicia el cliente.
3. El cliente puede enviar mensajes al servidor. Este respondera con el mismo mensaje pero en mayusculas. Existen la siguiente excepción:
    * Si el cliente manda el mensaje `Hola servidor`, el servidor contestará `HOLA CLIENTE`.
4. Para desconectar, el cliente puede enviar el mensaje `DESCONEXION`.

## Licencia

Este proyecto está licenciado bajo la Licencia GPLv3. Consulta el archivo `LICENSE` para más detalles.