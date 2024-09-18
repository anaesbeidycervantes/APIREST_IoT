# Importamos Flask, request, jsonify desde el paquete flask y requests para hacer peticiones HTTP.
from flask import Flask, request, jsonify
import requests

# Creamos una instancia de la clase Flask
app = Flask(__name__)

# URL base de la API externa (MockAPI)
API_URL = 'https://66eb042d55ad32cda47b5eb9.mockapi.io/IoTCarStatus'


# Definimos una ruta '/mensaje' que acepta los métodos GET, POST, PUT y DELETE.
@app.route('/mensaje', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manejar_mensajes():
    # Si el método de la solicitud es GET
    if request.method == 'GET':
        # Realizamos una solicitud GET a la API externa
        response = requests.get(API_URL)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "No se pudieron obtener los datos"}), response.status_code

    # Si el método de la solicitud es POST
    elif request.method == 'POST':
        # Obtenemos los datos enviados en el cuerpo de la solicitud
        nuevo_mensaje = request.get_json()
        # Realizamos una solicitud POST a la API externa
        response = requests.post(API_URL, json=nuevo_mensaje)
        if response.status_code == 201:
            return jsonify({"mensaje": "Método POST: Has enviado un nuevo mensaje a la base de datos."}), 201
        else:
            return jsonify({"error": "No se pudo crear el mensaje"}), response.status_code

    # Si el método de la solicitud es PUT
    elif request.method == 'PUT':
        # Obtenemos los datos enviados en el cuerpo de la solicitud
        mensaje_actualizado = request.get_json()
        # Especificamos un ID para actualizar un recurso en la API externa
        id_mensaje = mensaje_actualizado.get("id", None)  # Asegúrate de que el ID esté presente en el cuerpo
        if id_mensaje:
            # Realizamos una solicitud PUT a la API externa
            response = requests.put(f"{API_URL}/{id_mensaje}", json=mensaje_actualizado)
            if response.status_code == 200:
                return jsonify({"mensaje": "Método PUT: Has actualizado un mensaje existente."}), 200
            else:
                return jsonify({"error": "No se pudo actualizar el mensaje"}), response.status_code
        else:
            return jsonify({"error": "ID del mensaje no proporcionado."}), 400

    # Si el método de la solicitud es DELETE
    elif request.method == 'DELETE':
        # Obtenemos el ID del mensaje a eliminar desde la solicitud (por ejemplo, desde un parámetro en la URL)
        id_mensaje = request.args.get('id')  # El ID se enviará como un parámetro en la URL
        if id_mensaje:
            # Realizamos una solicitud DELETE a la API externa
            response = requests.delete(f"{API_URL}/{id_mensaje}")
            if response.status_code == 200:
                return jsonify({"mensaje": "Método DELETE: Has eliminado un mensaje."}), 200
            else:
                return jsonify({"error": "No se pudo eliminar el mensaje"}), response.status_code
        else:
            return jsonify({"error": "ID del mensaje no proporcionado."}), 400


# Iniciamos el servidor si este archivo es ejecutado directamente.
if __name__ == '__main__':
    app.run(debug=True)
