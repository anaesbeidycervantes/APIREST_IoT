from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL base de MockAPI para el recurso IoTCarStatus
MOCKAPI_URL = "https://66eb042d55ad32cda47b5eb9.mockapi.io/IoTCarStatus"


# GET: Obtener todos los registros o un registro específico por ID
@app.route('/iotcarstatus', methods=['GET'])
def get_status():
    # Si se pasa un ID en los parámetros de la URL, se obtiene ese registro
    record_id = request.args.get('id')
    if record_id:
        response = requests.get(f"{MOCKAPI_URL}/{record_id}")
    else:
        # Si no se pasa ningún ID, se obtienen todos los registros
        response = requests.get(MOCKAPI_URL)

    return jsonify(response.json()), response.status_code


# POST: Crear un nuevo registro
@app.route('/iotcarstatus', methods=['POST'])
def create_status():
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    # Enviar solicitud POST a MockAPI para crear un nuevo registro
    response = requests.post(MOCKAPI_URL, json=data)
    return jsonify(response.json()), response.status_code


# PUT: Actualizar un registro existente por ID
@app.route('/iotcarstatus', methods=['PUT'])
def update_status():
    # Obtener el ID del registro a actualizar desde los parámetros de la URL
    record_id = request.args.get('id')
    if not record_id:
        return jsonify({"error": "ID is required for updating a record"}), 400

    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    # Enviar solicitud PUT a MockAPI para actualizar el registro
    response = requests.put(f"{MOCKAPI_URL}/{record_id}", json=data)
    return jsonify(response.json()), response.status_code


# DELETE: Eliminar un registro por ID
@app.route('/iotcarstatus', methods=['DELETE'])
def delete_status():
    # Obtener el ID del registro a eliminar desde los parámetros de la URL
    record_id = request.args.get('id')
    if not record_id:
        return jsonify({"error": "ID is required for deleting a record"}), 400

    # Enviar solicitud DELETE a MockAPI para eliminar el registro
    response = requests.delete(f"{MOCKAPI_URL}/{record_id}")
    return jsonify({"message": "Record deleted successfully"}), response.status_code


# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
