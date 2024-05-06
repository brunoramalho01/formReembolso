from flask import Flask, render_template, request, redirect, url_for
from email_utils import send_email
from werkzeug.utils import secure_filename
import uuid
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

def generate_protocol_number():
    return str(uuid.uuid4().hex)[:8]  # Gera um número de protocolo único de 8 caracteres

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.form['nome']
        remetente = request.form['email']
        protocolo = generate_protocol_number()
        
        # Inicializa uma variável para o caminho do arquivo como None
        file_path = None

        # Verifica se o arquivo foi enviado
        if 'upload-comprovante' in request.files:
            file = request.files['upload-comprovante']
            if file.filename != '':  # Verifica se um arquivo foi selecionado
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

        # Passa os dados do formulário e o caminho do arquivo (se houver) para a função de envio de e-mail
        send_email(nome, protocolo, remetente, request.form, file_path=file_path)
        
        return redirect(url_for('success', protocolo=protocolo))
    return render_template('formulario.html')

@app.route('/success/<protocolo>')
def success(protocolo):
    return render_template('success.html', protocolo=protocolo)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)