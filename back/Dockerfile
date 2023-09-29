# Use a imagem base do Python
FROM python:3.8-alpine

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de aplicação para o diretório de trabalho
COPY app.py /app/

# Instale as dependências da aplicação (Flask neste caso)
RUN pip install Flask
RUN pip install Flask-CORS

# Exponha a porta em que o Flask estará em execução (a mesma que você configurou na aplicação Flask)
EXPOSE 80

# Comando para iniciar a aplicação Flask quando o contêiner for iniciado
CMD ["python", "app.py"]
