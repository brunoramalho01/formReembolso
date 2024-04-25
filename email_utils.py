import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD
from jinja2 import Template  # Importe o Template do Jinja2

def send_email(nome, protocolo, remetente, form_data):  # Adicione form_data como um parâmetro
    # Carrega o conteúdo do arquivo HTML
    with open('email_template.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())  # Carrega o template do Jinja2

    # Preenche os espaços reservados com os dados fornecidos
    body = template.render(nome=nome, protocolo=protocolo, form_data=form_data)  # Renderiza o template com os dados

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'bsantos@sescrr.com.br'  # Email do destinatário
    msg['Cc'] = remetente  # Cópia para o remetente
    msg['Subject'] = 'Nova Solicitação de ' + nome + 'Protocolo Nº: ' + protocolo

    # Anexa o corpo do e-mail à mensagem
    msg.attach(MIMEText(body, 'html'))

    # Configuração do servidor SMTP
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)

    # Envio do e-mail
    text = msg.as_string()
    server.sendmail(EMAIL_USER, ['bsantos@sescrr.com.br', remetente], text)  # Adiciona o remetente na lista de destinatários
    server.quit()
