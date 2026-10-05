# Discord Music Bot

Bot multifunción para Discord desarrollado como proyecto de **Desarrollo de Aplicaciones Multiplataforma (DAM)**.

El proyecto está centrado principalmente en la reproducción y gestión de música mediante **discord.py, Wavelink y Lavalink**, con persistencia de datos mediante **PostgreSQL**, internacionalización de mensajes y un sistema de eventos y logs.

## Características

* Reproducción de música en canales de voz.
* Búsqueda y reproducción de canciones.
* Gestión de la cola de reproducción.
* Pausar y reanudar la reproducción.
* Saltar canciones.
* Control de volumen.
* Repetición de canciones y cola.
* Aleatorización de la cola.
* Consulta de letras.
* Información de la canción actual.
* Comando de moderación.
* Configuración del servidor.
* Sistema de internacionalización (i18n).
* Persistencia mediante PostgreSQL.
* Procesamiento de audio mediante Lavalink.
* Sistema de logs.
* Entorno preparado para ejecutarse mediante Docker.
* Estructura de pruebas automatizadas mediante pytest.

---

# 1. Requisitos

Antes de instalar el proyecto necesitas:

* Git
* Docker
* Docker Compose
* Una cuenta de Discord
* Una aplicación/bot creado en el Discord Developer Portal

No es necesario instalar Python ni PostgreSQL en el sistema anfitrión si se utiliza el entorno Docker proporcionado por el proyecto.

---

# 2. Clonar el repositorio

Clona el repositorio:

```bash
git clone https://github.com/KevinUrreta/Discord_bot.git
```

Entra en la carpeta:

```bash
cd Discord_bot
```

---

# 3. Configuración del bot de Discord

Crea una aplicación desde el **Discord Developer Portal** y añade un bot.

Necesitarás obtener el token del bot y configurar los permisos necesarios para que pueda:

* Conectarse a servidores.
* Leer y enviar mensajes.
* Conectarse a canales de voz.
* Hablar en canales de voz.
* Utilizar las funciones necesarias para la reproducción de música.

## Intents

El bot utiliza los intents necesarios para gestionar los eventos de Discord.

El **Message Content Intent** debe estar habilitado porque el bot utiliza comandos mediante prefijo.

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

Los valores deben coincidir con la configuración utilizada por el proyecto.

### Importante

No publiques nunca el archivo `.env` en Git.

El token de Discord y las contraseñas deben mantenerse fuera del repositorio.

Comprueba que `.env` esté incluido en `.gitignore`.

---

# 5. Estructura del proyecto

La estructura principal del proyecto es:

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
│   ├── docs.py
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

La documentación de la arquitectura se encuentra en:

```text
docs/arch.md
```

---

# 6. Arquitectura

El código está dividido en diferentes módulos según su responsabilidad.

```text
src/
├── bot/
│   ├── commands/
│   ├── events/
│   └── tasks/
│
├── core/
├── database/
│   ├── models/
│   └── repositories/
│
├── helpers/
│
└── locales/
```

### `bot`

Contiene la lógica relacionada directamente con Discord:

* `commands/`: comandos del bot.
* `events/`: eventos de Discord y Wavelink.
* `tasks/`: tareas periódicas.

### `core`

Contiene componentes principales del funcionamiento del bot, como:

* Carga dinámica de módulos.
* Sistema de logs.
* Gestión del prefijo.
* Estado del reproductor.
* Utilidades relacionadas con el reproductor.

### `database`

Contiene la conexión con PostgreSQL, los modelos y los repositorios utilizados para acceder a los datos.

### `helpers`

Contiene funciones auxiliares reutilizables.

### `locales`

Contiene el sistema de internacionalización y los archivos de traducción.

La documentación completa de la arquitectura está disponible en:

```text
docs/arch.md
```

---

# 7. Ejecutar el proyecto con Docker

El proyecto está preparado para ejecutarse mediante Docker Compose.

Desde la raíz del proyecto:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Esto construirá la imagen del bot y arrancará los servicios definidos en `docker-compose.yml`.

Para comprobar el estado:

```bash
docker compose -f docker/docker-compose.yml ps
```

Los servicios principales son:

* `bot`
* `lavalink`
* `postgres`

El contenedor del bot se denomina `discord_bot`.

---

# 8. Comprobar los logs

Para consultar los logs de todos los servicios:

```bash
docker compose -f docker/docker-compose.yml logs -f
```

Para consultar únicamente el bot:

```bash
docker compose -f docker/docker-compose.yml logs -f bot
```

Para consultar Lavalink:

```bash
docker compose -f docker/docker-compose.yml logs -f lavalink
```

Para consultar PostgreSQL:

```bash
docker compose -f docker/docker-compose.yml logs -f postgres
```

---

# 9. Lavalink y Wavelink

El sistema de reproducción utiliza:

* **Lavalink** como servidor de audio.
* **Wavelink** como cliente para comunicarse con Lavalink.

La configuración de Lavalink se encuentra en:

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

El bot se conecta al servicio mediante:

```text
lavalink
```

utilizando el puerto:

```text
2333
```

Desde el contenedor del bot no se debe utilizar `localhost` para conectarse a Lavalink, ya que `localhost` hace referencia al propio contenedor.

---

# 10. PostgreSQL

El proyecto utiliza PostgreSQL para almacenar información relacionada con los servidores y miembros.

Dentro de Docker, la conexión se realiza utilizando el nombre del servicio:

```text
postgres
```

y el puerto:

```text
5432
```

Desde el contenedor del bot tampoco debe utilizarse `localhost` para acceder a PostgreSQL.

Puedes comprobar el estado de los servicios con:

```bash
docker compose -f docker/docker-compose.yml ps
```

---

# 11. Arranque de la aplicación

Una vez configurado el archivo `.env`, ejecuta:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Comprueba el estado:

```bash
docker compose -f docker/docker-compose.yml ps
```

Y consulta los logs del bot:

```bash
docker compose -f docker/docker-compose.yml logs -f bot
```

Durante el arranque, el bot debe:

1. Conectarse a Discord.
2. Conectarse a Lavalink.
3. Iniciar la sincronización de la base de datos.
4. Cargar los comandos, eventos y tareas.

---

# 12. Comandos disponibles

El bot utiliza comandos mediante **prefijo**.

El prefijo predeterminado es:

```text
!
```

## Configuración

```text
!language
!prefix
```

### `!language`

Permite consultar o modificar el idioma del servidor.

Ejemplo:

```text
!language es
```

### `!prefix`

Permite consultar o modificar el prefijo del servidor.

Ejemplo:

```text
!prefix <
```

---

## Moderación

```text
!clear
```

Permite eliminar mensajes según los permisos correspondientes.

---

## Música

```text
!join
!play
!pause
!resume
!stop
!skip
!queue
!remove
!clear
!leave
!loop
!shuffle
!volume
!nowplaying
!lyrics
```

### Ejemplos

Reproducir una canción:

```text
!play nombre de la canción
```

Consultar la cola:

```text
!queue
```

Pausar:

```text
!pause
```

Reanudar:

```text
!resume
```

Cambiar el volumen:

```text
!volume 50
```

Consultar la canción actual:

```text
!nowplaying
```

---

# 13. Internacionalización

El proyecto dispone de un sistema de internacionalización para adaptar los mensajes del bot a diferentes idiomas.

Actualmente están disponibles:

| Código | Idioma    |
| ------ | --------- |
| `de`   | Deutsch   |
| `en`   | English   |
| `es`   | Español   |
| `fr`   | Français  |
| `ja`   | 日本語       |
| `pt`   | Português |
| `ru`   | Русский   |
| `zh`   | 中文        |

Los archivos de traducción se encuentran en:

```text
src/locales/
```

Actualmente:

```text
de_DE.json
en_US.json
es_ES.json
fr_FR.json
ja_JP.json
pt_BR.json
ru_RU.json
zh_CN.json
```

La lógica de internacionalización se encuentra en:

```text
src/locales/i18n.py
```

Las traducciones se utilizan tanto en las respuestas del bot como en diferentes mensajes de logs.

---

# 14. Persistencia

El proyecto utiliza PostgreSQL para mantener información de los servidores y miembros.

Entre los datos gestionados se encuentran configuraciones como:

* Prefijo del servidor.
* Idioma del servidor.
* Información relacionada con los miembros.

La sincronización de la base de datos se realiza mediante:

```text
src/bot/tasks/database_sync.py
```

---

# 15. Logs

Los logs generados por la aplicación se almacenan en:

```text
logs/
```

Actualmente se utilizan:

```text
bot.log
database.log
errors.log
lavalink.log
wavelink.log
```

Cada archivo permite separar diferentes tipos de información generada durante la ejecución del proyecto.

---

# 16. Tests

El proyecto dispone de una estructura de pruebas basada en **pytest**.

Los tests se encuentran en:

```text
tests/
```

La estructura sigue la organización principal del código:

```text
tests/
└── src/
    ├── bot/
    ├── core/
    ├── database/
    ├── helpers/
    └── locales/
```

Para ejecutar las pruebas:

```bash
pytest
```

Para obtener información detallada:

```bash
pytest -v
```

Para ejecutar un archivo concreto:

```bash
pytest tests/src/core/test_core_loader.py
```

Para ejecutar únicamente las pruebas de los comandos de música:

```bash
pytest tests/src/bot/commands/music/
```

---

# 17. Acceder al contenedor del bot

Para acceder al contenedor:

```bash
docker exec -it discord_bot sh
```

Una vez dentro se puede comprobar la versión de Python:

```bash
python --version
```

También se pueden ejecutar los tests:

```bash
pytest
```

Para salir:

```bash
exit
```

---

# 18. Scripts auxiliares

La carpeta:

```text
scripts/
```

contiene diferentes scripts utilizados durante el desarrollo.

Actualmente incluye:

```text
docs.py
generate_events.py
generate_music_tests.py
generate_tests.py
```

Estos scripts facilitan tareas relacionadas con la documentación y la generación de estructuras de pruebas.

---

# 19. Detener la aplicación

Para detener los servicios:

```bash
docker compose -f docker/docker-compose.yml down
```

Esto detiene y elimina los contenedores, pero mantiene los volúmenes persistentes según la configuración de Docker Compose.

---

# 20. Eliminar los datos persistentes

**Precaución:** esta operación puede eliminar los datos persistentes de PostgreSQL.

Utilízala únicamente si quieres reiniciar completamente el entorno:

```bash
docker compose -f docker/docker-compose.yml down -v
```

---

# 21. Reconstruir el entorno

Después de realizar cambios en el código o en los Dockerfiles:

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

# 22. Desarrollo local

El proyecto también puede ejecutarse mediante un entorno virtual de Python.

Para crear uno nuevo en Windows:

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Después:

```powershell
python main.py
```

Para el funcionamiento completo del proyecto siguen siendo necesarios los servicios externos utilizados por la aplicación, especialmente PostgreSQL y Lavalink.

---

# 23. Solución de problemas

## El bot no inicia

Comprueba el estado de los servicios:

```bash
docker compose -f docker/docker-compose.yml ps
```

Consulta los logs:

```bash
docker compose -f docker/docker-compose.yml logs bot
```

Comprueba también que las variables del archivo `.env` sean correctas.

---

## Lavalink no conecta

Consulta sus logs:

```bash
docker compose -f docker/docker-compose.yml logs lavalink
```

Comprueba que el servicio esté activo:

```bash
docker compose -f docker/docker-compose.yml ps
```

Desde el bot, Lavalink debe utilizar:

```text
lavalink:2333
```

y no:

```text
localhost:2333
```

---

## No se reproduce música

Comprueba:

1. Que Lavalink esté iniciado.
2. Que Wavelink haya conectado correctamente.
3. Que el bot esté conectado a un canal de voz.
4. Que el bot tenga permisos para conectarse y hablar.
5. Los siguientes logs:

```text
logs/lavalink.log
logs/wavelink.log
logs/errors.log
```

---

## Error de conexión con PostgreSQL

Comprueba el estado:

```bash
docker compose -f docker/docker-compose.yml ps
```

Consulta los logs:

```bash
docker compose -f docker/docker-compose.yml logs postgres
```

Y revisa las variables:

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

---

# 24. Flujo rápido de instalación

Para instalar el proyecto desde cero:

```bash
git clone https://github.com/KevinUrreta/Discord_bot.git
cd Discord_bot
```

Crea y configura el archivo:

```text
.env
```

Después ejecuta:

```bash
docker compose -f docker/docker-compose.yml up -d --build
```

Comprueba los servicios:

```bash
docker compose -f docker/docker-compose.yml ps
```

Consulta los logs del bot:

```bash
docker compose -f docker/docker-compose.yml logs -f bot
```

Una vez iniciado, invita el bot a tu servidor de Discord y utiliza el prefijo configurado para ejecutar los comandos.

---

# 25. Tecnologías utilizadas

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

# 26. Documentación

La documentación técnica de la arquitectura del proyecto se encuentra en:

```text
docs/arch.md
```

Además, el código fuente contiene documentación mediante docstrings para facilitar su comprensión y mantenimiento.

---

# 27. Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

```text
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
```
