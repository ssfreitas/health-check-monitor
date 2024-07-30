# Usar a imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expor a porta que o Prometheus usará
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "metrics_exporter.py"]
