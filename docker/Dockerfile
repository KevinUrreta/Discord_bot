FROM python:3.14-slim

WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    tree \
    ffmpeg \
    curl \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

# Ejecuta el bot
CMD ["python", "main.py"]