FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8503

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8503"]
