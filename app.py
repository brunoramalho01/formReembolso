from flask import Flask, render_template, request, redirect, url_for
from email_utils import send_email
import uuid

app = Flask(__name__)

def generate_protocol_number():
    return str(uuid.uuid4().hex)[:8]  # Gera um número de protocolo único de 8 caracteres

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.form['nome']
        remetente = request.form['email']
        protocolo = generate_protocol_number()
        
        # Passa os dados para a função de envio de e-mail
        send_email(nome, protocolo, remetente, request.form)  # Adiciona request.form para capturar todos os dados do formulário
        return redirect(url_for('success', protocolo=protocolo))
    return render_template('formulario.html')

@app.route('/success/<protocolo>')
def success(protocolo):
    return render_template('success.html', protocolo=protocolo)

if __name__ == "__main__":
    app.run(debug=True)
