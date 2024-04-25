import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(nome, protocolo, remetente, form_data):
    # Carrega o conteúdo do arquivo HTML
    with open('email_template.html', 'r', encoding='utf-8') as file:
        body = file.read()

    # Preenche os espaços reservados com os dados fornecidos
    body = body.replace('{{ nome }}', nome)
    body = body.replace('{{ protocolo }}', protocolo)

    # Adiciona os dados do formulário ao corpo do e-mail
    for key, value in form_data.items():
        body = body.replace('{{ ' + key + ' }}', value)

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
