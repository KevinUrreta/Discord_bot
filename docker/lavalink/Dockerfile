# Imagen de descarga del contenedor
FROM ghcr.io/lavalink-devs/lavalink:4

USER root

# Instala dependencias
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3.11 python3.11-venv python3-pip \
    && python3.11 -m venv /opt/yt-dlp \
    && /opt/yt-dlp/bin/pip install --no-cache-dir yt-dlp \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/yt-dlp/bin:$PATH"

USER lavalink