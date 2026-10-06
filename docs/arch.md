```
(.venv) PS D:\Carpeta\Nueva carpeta> docker exec -it discord_bot sh
# tree -I "venv|__pycache__|postgres_data"
.
|-- LICENSE
|-- README.md
|-- docker
|   |-- docker-compose.yml
|   `-- dockerfile
|-- docs
|   `-- arch.md
|-- lavalink
|   |-- application.yml
|   |-- dockerfile
|   `-- plugins
|       |-- lavasrc-plugin-4.8.3.jar
|       `-- youtube-plugin-1.18.2.jar
|-- logs
|   |-- app.log
|   |-- bot.log
|   |-- database.log
|   |-- errors.log
|   |-- lavalink.log
|   |-- lavalink.log.2026-10-05.0.gz
|   `-- wavelink.log
|-- main.py
|-- pytest.ini
|-- requirements.txt
|-- scripts
|   |-- docs.py
|   |-- generate_events.py
|   |-- generate_music_tests.py
|   `-- generate_tests.py
|-- src
|   |-- app
|   |   |-- commands
|   |   |   |-- config
|   |   |   |   |-- language.py
|   |   |   |   `-- prefix.py
|   |   |   |-- moderation
|   |   |   |   `-- clear.py
|   |   |   `-- music
|   |   |       |-- clear.py
|   |   |       |-- join.py
|   |   |       |-- leave.py
|   |   |       |-- loop.py
|   |   |       |-- lyrics.py
|   |   |       |-- now_playing.py
|   |   |       |-- pause.py
|   |   |       |-- play.py
|   |   |       |-- queue.py
|   |   |       |-- remove.py
|   |   |       |-- resume.py
|   |   |       |-- shuffle.py
|   |   |       |-- skip.py
|   |   |       |-- stop.py
|   |   |       `-- volume.py
|   |   |-- events
|   |   |   |-- application
|   |   |   |   |-- on_application_command_error.py
|   |   |   |   |-- on_command.py
|   |   |   |   |-- on_command_error.py
|   |   |   |   |-- on_connect.py
|   |   |   |   |-- on_disconnect.py
|   |   |   |   |-- on_ready.py
|   |   |   |   |-- on_resumed.py
|   |   |   |   `-- on_webhook_update.py
|   |   |   |-- guild
|   |   |   |   |-- on_guild_channel_create.py
|   |   |   |   |-- on_guild_channel_delete.py
|   |   |   |   |-- on_guild_channel_update.py
|   |   |   |   |-- on_guild_emojis_update.py
|   |   |   |   |-- on_guild_join.py
|   |   |   |   |-- on_guild_remove.py
|   |   |   |   |-- on_guild_role_create.py
|   |   |   |   |-- on_guild_role_delete.py
|   |   |   |   |-- on_guild_role_update.py
|   |   |   |   `-- on_guild_stickers_update.py
|   |   |   |-- member
|   |   |   |   |-- on_member_join.py
|   |   |   |   |-- on_member_remove.py
|   |   |   |   |-- on_member_update.py
|   |   |   |   `-- on_user_update.py
|   |   |   |-- message
|   |   |   |   |-- on_message.py
|   |   |   |   |-- on_message_delete.py
|   |   |   |   |-- on_message_edit.py
|   |   |   |   |-- on_raw_reaction_add.py
|   |   |   |   |-- on_raw_reaction_remove.py
|   |   |   |   |-- on_reaction_add.py
|   |   |   |   |-- on_reaction_clear.py
|   |   |   |   |-- on_reaction_remove.py
|   |   |   |   `-- on_typing.py
|   |   |   |-- voice
|   |   |   |   |-- on_wavelink_track_end.py
|   |   |   |   `-- on_wavelink_track_start.py
|   |   |   `-- wavelink
|   |   |       `-- on_voice_state_update.py
|   |   `-- tasks
|   |       `-- database_sync.py
|   |-- core
|   |   |-- config.py
|   |   |-- loader.py
|   |   |-- logging.py
|   |   |-- player_state.py
|   |   `-- prefix.py
|   |-- helpers
|   |   |-- embeds.py
|   |   |-- formatting.py
|   |   |-- music_utils.py
|   |   `-- permissions.py
|   |-- i18n
|   |   |-- locales
|   |   |   |-- de_DE.json
|   |   |   |-- en_US.json
|   |   |   |-- es_ES.json
|   |   |   |-- fr_FR.json
|   |   |   |-- ja_JP.json
|   |   |   |-- pt_BR.json
|   |   |   |-- ru_RU.json
|   |   |   `-- zh_CN.json
|   |   `-- translator.py
|   `-- infrastructure
|       |-- database
|       |   |-- __init__.py
|       |   |-- connection.py
|       |   |-- migrations
|       |   |-- models
|       |   |   |-- guild.py
|       |   |   `-- member.py
|       |   `-- repositories
|       |       |-- __init__.py
|       |       |-- guild.py
|       |       `-- member.py
|       `-- lavalink
|           `-- connection.py
`-- tests
    |-- e2e
    |-- integration
    `-- unit

35 directories, 102 files
```