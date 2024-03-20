from flask import Flask, render_template, request
import serial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enviar-dados', methods=['POST'])
def enviar_dados():
    porta_serial = serial.Serial('COM7', 9600)  # Substitua '/dev/ttyS0' pela porta correta e 9600 pela taxa de transmissão desejada

    dados = request.form['dados']  # Obtenha os dados do formulário HTML
    porta_serial.write(dados.encode())  # Envie os dados após convertê-los para bytes

    porta_serial.close()

    return 'Dados enviados com sucesso!'

if __name__ == "__main__":
    app.run()