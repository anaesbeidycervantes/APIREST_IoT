from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para el endpoint de la API
# se le indica al lenguaje a donde se dirige el usuario para utilizar la aplicacion, la ruta donde se va a programar
@app.route('/saludo', methods=['GET'])
def saludo():
    #mensaje que mostrara la respuesta
    return '¡Hola! Bienvenido a mi API'

# Iniciar el servidor, ejecuta el programa principal del apiget
# app es el decorador que se creo con flask
#se ejecuta en modo depuracion
if __name__ == '__main__':
    app.run(debug=True)
