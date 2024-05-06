import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD
from jinja2 import Template  # Importe o Template do Jinja2

def send_email(nome, protocolo, remetente, form_data, file_path=None):  # Adicione form_data como um parâmetro
    # Converta form_data para um dicionário mutável
    form_data = form_data.to_dict()

    # Carrega o conteúdo do arquivo HTML
    with open('email_template.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())  # Carrega o template do Jinja2
    
    # Substitua 'on' por 'Sim' e inclua o texto dos termos
    form_data['termos_reembolso'] = "Sim, estou ciente que as solicitações de Reembolso enviados através deste link passarão por análise e que sua aprovação está condicionada aos critérios estabelecidos em contratos e políticas internas."
    form_data['termos_lgpd'] = "Sim, em observância à Lei n°. 13.709/18 - Lei Geral de Proteção de Dados Pessoais e seus dispositivos aplicáveis, manifesto de forma expressa, livre e consciente, no sentido de autorizar o SESC/DR/RR a realizar o tratamento dos meus dados pessoais."
    
    # Remova a resposta do reCAPTCHA
    form_data.pop('g-recaptcha-response', None)

    # Preenche os espaços reservados com os dados fornecidos
    body = template.render(nome=nome, protocolo=protocolo, form_data=form_data)  # Renderiza o template com os dados

    # Configuração da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'crc@sescrr.com.br'  # Email do destinatário
    msg['Cc'] = remetente  # Cópia para o remetente
    msg['Subject'] = 'Solicitação Reembolso de ' + nome + ' | Protocolo Nº: ' + protocolo

    # Anexa o arquivo, se presente
    if file_path:
        with open(file_path, 'rb') as file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(part)

    # Anexa o corpo do e-mail à mensagem
    msg.attach(MIMEText(body, 'html'))

    # Configuração do servidor SMTP
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)

    # Envio do e-mail
    text = msg.as_string()
    server.sendmail(EMAIL_USER, ['crc@sescrr.com.br', remetente], text)  # Adiciona o remetente na lista de destinatários
    server.quit()
