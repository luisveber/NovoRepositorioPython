#Aplicação Flask Leitor QRCODE

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
usuario = "LUIS HENRIQUE VEBER"
@app.route("/")
def index():
    return render_template("index.html",usuario=usuario)

@app.route("/verificar", methods=["POST"])
def verificar():
    # Conexão com o banco de dados
    conn = mysql.connector.connect(
    host ="auth-db727.hstgr.io",
    user = "u652056245_luisveber",
    password = "Semprom2014",
    database = "u652056245_Teste"
    )

    # Cursor para executar as operações no banco de dados
    cursor = conn.cursor()


    # Texto digitado pelo usuário
    texto = request.form.get("texto")

    # Verificação de cadastro
    query = "SELECT * FROM qrcode WHERE qrcode = %s"
    cursor.execute(query, (texto,))
    resultado = cursor.fetchall()

    if len(resultado) > 0:
        query = "SELECT * FROM qrcode ORDER BY  id DESC"
        cursor.execute(query)
        registros = cursor.fetchall()
        mensagem = "Texto já está cadastrado."
    else:
        # Cadastro do texto
        query = "INSERT INTO qrcode (qrcode) VALUES (%s)"
        cursor.execute(query, (texto,))
        conn.commit()
        quety = "SELECT * FROM qrcode ORDER BY id DESC"
        cursor.execute(quety)
        registros = cursor.fetchall()
        mensagem = "Texto cadastrado com sucesso."

    # Fecha a conexão com o banco de dados
    conn.close()

    return render_template("resultado.html", mensagem=mensagem,registros=registros,texto=texto, usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)