# Discord Music Bot

Bot multifunción para Discord desarrollado como proyecto de **Desarrollo de Aplicaciones Multiplataforma (DAM)**.

Actualmente el proyecto está centrado principalmente en la reproducción y gestión de música mediante **Discord.py + Wavelink + Lavalink**, con persistencia de datos mediante **PostgreSQL** e internacionalización de mensajes.

---

## Características

* 🎵 Reproducción de música en canales de voz.
* 🔎 Búsqueda y reproducción de canciones.
* 📋 Gestión de cola de reproducción.
* ⏯️ Controles de reproducción.
* 🔊 Control de volumen.
* 🔁 Repetición de canciones o cola.
* 🔀 Aleatorización de la cola.
* 🎤 Consulta de letras.
* 🎶 Información de la canción actual.
* 🛡️ Comandos de moderación.
* ⚙️ Configuración del servidor.
* 🌐 Sistema de internacionalización (i18n).
* 💾 Persistencia mediante PostgreSQL.
* 🔌 Lavalink para el procesamiento de audio.
* 📝 Sistema de logs.
* 🧪 Tests automatizados con pytest.
* 🐳 Entorno preparado para ejecutarse mediante Docker.

---

# 1. Requisitos

Antes de instalar el proyecto necesitas tener instalados:

* Git
* Docker
* Docker Compose
* Una cuenta de Discord
* Un bot de Discord creado en el Developer Portal

No es necesario instalar Python ni PostgreSQL en el sistema anfitrión si se utiliza el entorno Docker proporcionado por el proyecto.

---

# 2. Clonar el repositorio

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Entra en la carpeta:

```bash
cd Discord_bot
```

Si el proyecto se encuentra en otra ubicación, utiliza la ruta correspondiente.

---

# 3. Configuración del bot de Discord

Crea una aplicación desde el **Discord Developer Portal** y añade un bot.

Necesitarás obtener:

* Token del bot.
* Client ID / Application ID.
* Los permisos necesarios para que el bot pueda conectarse a servidores y canales de voz.

## Intents

En la configuración del bot deben habilitarse los intents que utilice la aplicación.

Como mínimo, comprueba los intents relacionados con:

* Guilds
* Guild Members
* Guild Messages
* Message Content
* Guild Voice States

El `Message Content Intent` debe estar habilitado si el bot utiliza comandos mediante prefijo.

---

# 4. Variables de entorno

El proyecto utiliza un archivo `.env` para almacenar la configuración sensible.

Crea el archivo:

```text
.env
```

en la raíz del proyecto.

Ejemplo:

```env
DISCORD_TOKEN=TU_TOKEN_DE_DISCORD

POSTGRES_DB=discord_bot
POSTGRES_USER=discord_bot
POSTGRES_PASSWORD=TU_PASSWORD

POSTGRES_HOST=postgres
POSTGRES_PORT=5432

LAVALINK_HOST=lavalink
LAVALINK_PORT=2333
LAVALINK_PASSWORD=TU_PASSWORD
```

> Los nombres exactos de las variables deben coincidir con los utilizados por `docker-compose.yml`, `main.py` y el código de configuración del proyecto.

### Importante

No publiques nunca el archivo `.env` en Git.

Comprueba que `.env` está incluido en `.gitignore`.

---

# 5. Estructura principal

La aplicación está organizada de la siguiente forma:

```text
.
├── docker/
│   ├── docker-compose.yml
│   └── dockerfile
│
├── docs/
│   └── arch.md
│
├── lavalink/
│   ├── application.yml
│   ├── dockerfile
│   └── plugins/
│       ├── lavasrc-plugin-4.8.3.jar
│       └── youtube-plugin-1.18.2.jar
│
├── logs/
│   ├── bot.log
│   ├── database.log
│   ├── errors.log
│   ├── lavalink.log
│   └── wavelink.log
│
├── scripts/
│   ├── generate_events.py
│   ├── generate_music_tests.py
│   └── generate_tests.py
│
├── src/
│   ├── bot/
│   │   ├── commands/
│   │   ├── events/
│   │   └── tasks/
│   │
│   ├── core/
│   ├── database/
│   ├── helpers/
│   └── locales/
│
├── tests/
├── main.py
├── pytest.ini
└── requirements.txt
```

La documentación completa de la arquitectura se encuentra en:

```text
docs/arch.md
```

---

# 6. Levantar el entorno con Docker

El proyecto está preparado para ejecutarse mediante Docker Compose.

Desde la raíz del proyecto:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Esto construirá las imágenes necesarias y arrancará los servicios definidos en `docker-compose.yml`.

Para comprobar los contenedores:

```bash
docker compose -f docker/docker-compose.yml ps
```

---

# 7. Comprobar los logs

Para consultar los logs de Docker:

```bash
docker compose -f docker/docker-compose.yml logs -f
```

Para consultar únicamente el bot:

```bash
docker compose -f docker/docker-compose.yml logs -f discord_bot
```

Para consultar Lavalink:

```bash
docker compose -f docker/docker-compose.yml logs -f lavalink
```

---

# 8. Acceder al contenedor del bot

Para entrar en el contenedor:

```bash
docker exec -it discord_bot sh
```

Una vez dentro puedes comprobar la estructura:

```bash
tree -I "venv|__pycache__|postgres_data"
```

También puedes comprobar que Python está disponible:

```bash
python --version
```

---

# 9. Lavalink

El bot utiliza **Lavalink** como servidor de audio y **Wavelink** como cliente.

La configuración principal de Lavalink se encuentra en:

```text
lavalink/application.yml
```

Los plugins utilizados se encuentran en:

```text
lavalink/plugins/
```

Actualmente se incluyen:

```text
lavasrc-plugin-4.8.3.jar
youtube-plugin-1.18.2.jar
```

El bot se conecta al servicio Lavalink mediante el nombre del servicio Docker:

```text
lavalink
```

y el puerto:

```text
2333
```

Por ello, desde el contenedor del bot **no se debe utilizar `localhost` para conectarse a Lavalink**.

---

# 10. PostgreSQL

La aplicación utiliza PostgreSQL para almacenar información relacionada con los servidores y miembros.

Dentro de Docker, el bot debe conectarse al servicio PostgreSQL utilizando el nombre del servicio definido en `docker-compose.yml`.

La conexión no debe utilizar:

```text
localhost
```

desde el contenedor del bot.

Utiliza el nombre del servicio Docker correspondiente, por ejemplo:

```text
postgres
```

Puedes comprobar los servicios activos mediante:

```bash
docker compose -f docker/docker-compose.yml ps
```

---

# 11. Ejecutar la aplicación

Una vez iniciados los contenedores:

```bash
docker compose -f docker/docker-compose.yml up -d
```

Comprueba los logs del bot:

```bash
docker compose -f docker/docker-compose.yml logs -f discord_bot
```

Si el bot se ha iniciado correctamente, debería conectarse a Discord y posteriormente establecer la conexión con Lavalink.

---

# 12. Comandos disponibles

## Configuración

```text
/language
/prefix
```

Permiten configurar determinados aspectos del servidor.

## Moderación

```text
/clear
```

Permite gestionar mensajes según los permisos correspondientes.

## Música

```text
/play
/pause
/resume
/stop
/skip
/queue
/remove
/clear
/join
/leave
/loop
/shuffle
/volume
/now_playing
/lyrics
```

La disponibilidad de los comandos depende de la configuración del bot y de los permisos del usuario.

---

# 13. Internacionalización

El proyecto dispone de un sistema de internacionalización.

Los idiomas disponibles actualmente son:

```text
de_DE
en_US
es_ES
fr_FR
it_IT
ja_JP
nl_NL
pl_PL
pt_PT
```

Los archivos de traducción se encuentran en:

```text
src/locales/
```

Por ejemplo:

```text
src/locales/es_ES.json
src/locales/en_US.json
```

La lógica de traducción se encuentra en:

```text
src/locales/i18n.py
```

Las traducciones se utilizan tanto para las respuestas del bot como para diferentes logs internos.

---

# 14. Logs

Los logs se almacenan en:

```text
logs/
```

Actualmente existen diferentes archivos según el tipo de información:

```text
bot.log
database.log
errors.log
lavalink.log
wavelink.log
```

Esto permite separar la información generada por las diferentes partes de la aplicación.

---

# 15. Ejecutar los tests

El proyecto utiliza `pytest`.

Si ejecutas las pruebas dentro del entorno Python:

```bash
pytest
```

Para obtener información más detallada:

```bash
pytest -v
```

Para ejecutar un archivo concreto:

```bash
pytest tests/src/core/test_core_loader.py
```

Para ejecutar una categoría concreta, por ejemplo los comandos de música:

```bash
pytest tests/src/bot/commands/music/
```

---

# 16. Ejecutar tests dentro de Docker

Si el entorno Python está dentro del contenedor del bot:

```bash
docker exec -it discord_bot sh
```

y posteriormente:

```bash
pytest
```

Para salir del contenedor:

```bash
exit
```

Estos scripts están destinados a facilitar la creación y actualización de la estructura de pruebas.

---

# 17. Detener la aplicación

Para detener los servicios:

```bash
docker compose -f docker/docker-compose.yml down
```

Esto detiene y elimina los contenedores, pero no necesariamente elimina los volúmenes de datos.

---

# 18. Detener y eliminar los datos

**Precaución:** esta operación puede eliminar los datos persistentes de PostgreSQL dependiendo de la configuración de Docker Compose.

No utilices esta opción salvo que quieras reiniciar completamente el entorno.

```bash
docker compose -f docker/docker-compose.yml down -v
```

---

# 19. Reconstruir completamente el entorno

Si has realizado cambios en el código o en los Dockerfiles:

```bash
docker compose -f docker/docker-compose.yml down
```

Después:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Para comprobar el estado:

```bash
docker compose -f docker/docker-compose.yml ps
```

---

# 20. Desarrollo local sin Docker

El proyecto también contiene un entorno virtual de Python:

```text
.venv/
```

Para crear uno nuevo:

### Windows

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Después se puede ejecutar:

```powershell
python main.py
```

> Para el funcionamiento completo del proyecto siguen siendo necesarios los servicios externos utilizados por la aplicación, especialmente PostgreSQL y Lavalink.

---

# 21. Actualizar el proyecto

Si el proyecto ya está clonado:

```bash
git pull
```

Después de actualizar dependencias:

```bash
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up -d --build
```

---

# 22. Solución de problemas

## El bot no inicia

Comprueba los logs:

```bash
docker compose -f docker/docker-compose.yml logs discord_bot
```

Comprueba también que las variables del `.env` sean correctas.

---

## Lavalink no conecta

Comprueba:

```bash
docker compose -f docker/docker-compose.yml logs lavalink
```

Y comprueba que el contenedor esté funcionando:

```bash
docker compose -f docker/docker-compose.yml ps
```

Desde el bot, Lavalink debe utilizar el nombre del servicio Docker y no `localhost`.

---

## No se reproduce música

Comprueba primero:

1. Que Lavalink esté iniciado.
2. Que Wavelink haya conectado correctamente.
3. Que el bot esté conectado a un canal de voz.
4. Que el bot tenga permisos para conectarse y hablar.
5. Los archivos:

```text
logs/lavalink.log
logs/wavelink.log
logs/errors.log
```

---

## Error de conexión con PostgreSQL

Comprueba:

```bash
docker compose -f docker/docker-compose.yml ps
```

y los logs:

```bash
docker compose -f docker/docker-compose.yml logs postgres
```

Revisa también las variables:

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

---

# 23. Flujo rápido de instalación

Para una instalación nueva:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Discord_bot
```

Crear `.env`:

```text
.env
```

Configurar las variables necesarias.

Después:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Comprobar:

```bash
docker compose -f docker/docker-compose.yml ps
```

Ver logs:

```bash
docker compose -f docker/docker-compose.yml logs -f discord_bot
```

Ejecutar tests:

```bash
docker exec -it discord_bot sh
pytest
```

Salir:

```bash
exit
```

---

# 24. Tecnologías utilizadas

* Python
* discord.py
* Wavelink
* Lavalink
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose
* pytest
* python-dotenv
* PyNaCl
* yt-dlp
* Spotipy

---

# 25. Estructura de desarrollo

La aplicación separa diferentes responsabilidades:

```text
src/
├── bot/
│   ├── commands/
│   ├── events/
│   └── tasks/
│
├── core/
│
├── database/
│   ├── models/
│   └── repositories/
│
├── helpers/
│
└── locales/
```

Esta separación permite mantener independientes los comandos de Discord, eventos, lógica principal, acceso a datos, utilidades e internacionalización.

Para consultar la arquitectura completa:

```text
docs/arch.md
```

---

# 26. Licencia

MIT License

Copyright (c) 2024 KevinUrreta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
