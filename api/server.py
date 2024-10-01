from flask import Flask, request, Response
from config import API_TOKEN

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=["GET"])
def home():
    return "ready"


@app.route('/newalert', methods=["POST"])
def notify():
    headers = request.headers
    if not headers.get('authorization'):
        return Response("Unauthorized", 401)
    else:
        if headers.get('authorization') == 'Baerer {}'.format(API_TOKEN):
            try:
                if request.form.get('type') == 'hola':
                    type = request.form.get('type')
                    bank = request.form.get('bank')
                    phone = request.form.get('phone')
                    text = request.form.get('text')
                    mensaje = '''
                        <h1>Alerta enviada</h1>
                        <h1>The Tipo value is: {}</h1>
                        <h1>The Banco value is: {}</h1>
                        <h1>The Telefono value is: {}</h1>
                        <h1>The Texto value is: {}</h1>
                        '''.format(type, bank, phone, text)

                    return Response(mensaje, 200)
                else:
                    return Response('El usuario con telefono: {} no existe en la BD'
                                    .format(phone), 201)
            except Exception as e:
                print(e)
                return Response('Error', 500)
        else:
            return Response('El token es invalido', 400)


app.run()
