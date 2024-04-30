# Um dockerfile sempre deve começar importando a imagem de base.
# Usamos a palavra-chave 'FROM' para isso.
# Em nosso exemplo, queremos importar a imagem do python.
# Assim, escrevemos 'python' para o nome da imagem e 'latest' para  a versão.
FROM python:latest
# Defina o diretório de trabalho
# Para lançar nosso código em Python, devemos importá-lo em nossa imagem.
# Usamos para isso a palavra-chave 'COPY'.
# O primeiro parâmetro, 'main.py', é o nome do arquivo no host.
# O segundo parâmetro, '/', é o caminho onde colocar o arquivo na imagem.
# Aqui, colocamos o arquivo na pasta raiz da imagem.
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#Instale as dependência
# Exponha a porta que o seu aplicativo usa

# Precisamos definir o comando para lançar quando rodarmos a imagem.
# Usamos a palavra-chave 'CMD' para isso.
# O comando a seguir executará "python ./main.py".
CMD [ "python", "app.py" ]
