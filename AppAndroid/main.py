import kivy
import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime


kivy.require("1.11.1")

class ConsultaApp(App):

    def build(self):
        self.conn = mysql.connector.connect(
            host="auth-db727.hstgr.io",
            user="u652056245_flxluis",
            password="Semprom2014",
            database="u652056245_flx",
        )

        layout = BoxLayout(orientation="vertical")
        self.cnpj_input = TextInput(hint_text="CNPJ")
        self.nome_input = TextInput(hint_text="Nome")
        self.salvar_button = Button(text="Start")
        self.salvar_button.bind(on_press=self.salvar_consulta)
        self.resultado_label = Label()
        self.consultar_button = Button(text="Consultar Consultas")
        self.finalizar_button = Button(text="Finalizar")
        self.consultar_button.bind(on_press=self.consultar_consultas)
        self.finalizar_button.bind(on_press=self.finalizar)

        layout.add_widget(self.cnpj_input)
        layout.add_widget(self.nome_input)
        layout.add_widget(self.salvar_button)
        layout.add_widget(self.resultado_label)
        layout.add_widget(self.consultar_button)
        layout.add_widget(self.finalizar_button)

        return layout

    def salvar_consulta(self, instance):
        cursor = self.conn.cursor()
        cnpj = self.cnpj_input.text
        nome = self.nome_input.text
        data = datetime.datetime.now()

        # Insira os dados na tabela
        query = "INSERT INTO TbClientes (cnpj, nome, datacriacao) VALUES (%s, %s, %s)"
        cursor.execute(query, (cnpj, nome, data))
        self.conn.commit()

        self.cnpj_input.text = ""
        self.nome_input.text = ""

        self.resultado_label.text = "Consulta salva com sucesso."
    def finalizar(self, instance):
        cursor = self.conn.cursor()
        cnpj = self.cnpj_input.text
        data = datetime.datetime.now()

        query = "UPDATE TbClientes SET datafinalizacao = %s WHERE cnpj = %s"
        valores = (data, cnpj)
        cursor.execute(query, valores)
        self.conn.commit()
        self.cnpj_input.text = ""
        self.nome_input.text = ""

        self.resultado_label.text = "Edicao feita com sucesso."


    def consultar_consultas(self, instance):
        cursor = self.conn.cursor()

        # Consulte os dados na tabela
        query = "SELECT cnpj, nome, datacriacao, datafinalizacao FROM TbClientes"
        cursor.execute(query)

        consultas = cursor.fetchall()

        if consultas:
            resultado = "Consultas:\n"
            for consulta in consultas:
                resultado += f"CNPJ: {consulta[0]}, Nome: {consulta[1]}, Data: {consulta[2]}, Data Finalizacao: {consulta[3]}\n"
        else:
            resultado = "Nenhuma consulta encontrada."

        self.resultado_label.text = resultado

if __name__ == "__main__":
    app = ConsultaApp()
    app.run()

