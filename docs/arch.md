```
(.venv) PS D:\Carpeta\Nueva carpeta> docker exec -it discord_bot sh
# tree -I "venv|__pycache__|postgres_data"
.
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
|   |-- bot.log
|   |-- database.log
|   |-- errors.log
|   |-- lavalink.log
|   `-- wavelink.log
|-- main.py
|-- pytest.ini
|-- requirements.txt
|-- scripts
|   |-- generate_events.py
|   |-- generate_music_tests.py
|   `-- generate_tests.py
|-- src
|   |-- bot
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
|   |   |   `-- other
|   |   |       |-- on_application_command_error.py
|   |   |       |-- on_command.py
|   |   |       |-- on_command_error.py
|   |   |       |-- on_connect.py
|   |   |       |-- on_disconnect.py
|   |   |       |-- on_ready.py
|   |   |       |-- on_resumed.py
|   |   |       |-- on_voice_state_update.py
|   |   |       |-- on_wavelink_track_end.py
|   |   |       |-- on_wavelink_track_start.py
|   |   |       `-- on_webhook_update.py
|   |   `-- tasks
|   |       `-- database_sync.py
|   |-- core
|   |   |-- __init__.py
|   |   |-- loader.py
|   |   |-- logging.py
|   |   |-- player_state.py
|   |   `-- player_utils.py
|   |-- database
|   |   |-- __init__.py
|   |   |-- connection.py
|   |   |-- models
|   |   |   |-- guild.py
|   |   |   `-- member.py
|   |   `-- repositories
|   |       |-- guild.py
|   |       `-- member.py
|   |-- helpers
|   |   |-- __init__.py
|   |   |-- embeds.py
|   |   |-- music_utils.py
|   |   `-- permissions.py
|   `-- locales
|       |-- de_DE.json
|       |-- en_US.json
|       |-- es_ES.json
|       |-- fr_FR.json
|       |-- i18n.py
|       |-- it_IT.json
|       |-- ja_JP.json
|       |-- nl_NL.json
|       |-- pl_PL.json
|       `-- pt_PT.json
`-- tests
    |-- conftest.py
    `-- src
        |-- bot
        |   |-- commands
        |   |   |-- config
        |   |   |   |-- test_language.py
        |   |   |   `-- test_prefix.py
        |   |   |-- moderation
        |   |   |   `-- test_cls.py
        |   |   `-- music
        |   |       |-- test_clear.py
        |   |       |-- test_join.py
        |   |       |-- test_leave.py
        |   |       |-- test_loop.py
        |   |       |-- test_pause.py
        |   |       |-- test_play.py
        |   |       |-- test_queue.py
        |   |       |-- test_remove.py
        |   |       |-- test_resume.py
        |   |       |-- test_shuffle.py
        |   |       |-- test_skip.py
        |   |       |-- test_stop.py
        |   |       `-- test_volume.py
        |   |-- events
        |   |   |-- guild
        |   |   |   |-- test_on_guild_channel_create.py
        |   |   |   |-- test_on_guild_channel_delete.py
        |   |   |   |-- test_on_guild_channel_update.py
        |   |   |   |-- test_on_guild_emojis_update.py
        |   |   |   |-- test_on_guild_join.py
        |   |   |   |-- test_on_guild_remove.py
        |   |   |   |-- test_on_guild_role_create.py
        |   |   |   |-- test_on_guild_role_delete.py
        |   |   |   |-- test_on_guild_role_update.py
        |   |   |   `-- test_on_guild_stickers_update.py
        |   |   |-- member
        |   |   |   |-- test_on_member_join.py
        |   |   |   |-- test_on_member_remove.py
        |   |   |   |-- test_on_member_update.py
        |   |   |   `-- test_on_user_update.py
        |   |   |-- message
        |   |   |   |-- test_on_message.py
        |   |   |   |-- test_on_message_delete.py
        |   |   |   |-- test_on_message_edit.py
        |   |   |   |-- test_on_raw_reaction_add.py
        |   |   |   |-- test_on_raw_reaction_remove.py
        |   |   |   |-- test_on_reaction_add.py
        |   |   |   |-- test_on_reaction_clear.py
        |   |   |   |-- test_on_reaction_remove.py
        |   |   |   `-- test_on_typing.py
        |   |   `-- other
        |   |       |-- test_on_application_command_error.py
        |   |       |-- test_on_command.py
        |   |       |-- test_on_command_error.py
        |   |       |-- test_on_connect.py
        |   |       |-- test_on_disconnect.py
        |   |       |-- test_on_ready.py
        |   |       |-- test_on_resumed.py
        |   |       |-- test_on_voice_state_update.py
        |   |       |-- test_on_wavelink_track_end.py
        |   |       |-- test_on_wavelink_track_start.py
        |   |       `-- test_on_webhook_update.py
        |   `-- tasks
        |       `-- test_database_sync.py
        |-- core
        |   `-- test_player.py
        |-- database
        |   |-- repositories
        |   |   |-- test_guild_repository.py
        |   |   `-- test_member_repository.py
        |   `-- test_connection.py
        |-- helpers
        |   `-- test_checkers.py
        `-- locales
            `-- test_i18n.py

44 directories, 159 files
```