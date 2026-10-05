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
|   |-- bot.log
|   |-- database.log
|   |-- errors.log
|   |-- lavalink.log
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
|   |   |-- player_utils.py
|   |   `-- prefix.py
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
|   |   |-- formatting.py
|   |   |-- music_utils.py
|   |   `-- permissions.py
|   `-- locales
|       |-- de_DE.json
|       |-- en_US.json
|       |-- es_ES.json
|       |-- fr_FR.json
|       |-- i18n.py
|       |-- ja_JP.json
|       |-- pt_BR.json
|       |-- ru_RU.json
|       `-- zh_CN.json
`-- tests
    |-- conftest.py
    `-- src
        |-- bot
        |   |-- commands
        |   |   |-- config
        |   |   |   |-- test_bot_commands_config_language.py
        |   |   |   `-- test_bot_commands_config_prefix.py
        |   |   |-- moderation
        |   |   |   `-- test_bot_commands_moderation_clear.py
        |   |   `-- music
        |   |       |-- test_bot_commands_music_clear.py
        |   |       |-- test_bot_commands_music_join.py
        |   |       |-- test_bot_commands_music_leave.py
        |   |       |-- test_bot_commands_music_loop.py
        |   |       |-- test_bot_commands_music_lyrics.py
        |   |       |-- test_bot_commands_music_now_playing.py
        |   |       |-- test_bot_commands_music_pause.py
        |   |       |-- test_bot_commands_music_play.py
        |   |       |-- test_bot_commands_music_queue.py
        |   |       |-- test_bot_commands_music_remove.py
        |   |       |-- test_bot_commands_music_resume.py
        |   |       |-- test_bot_commands_music_shuffle.py
        |   |       |-- test_bot_commands_music_skip.py
        |   |       |-- test_bot_commands_music_stop.py
        |   |       `-- test_bot_commands_music_volume.py
        |   |-- events
        |   |   |-- guild
        |   |   |   |-- test_bot_events_guild_on_guild_channel_create.py
        |   |   |   |-- test_bot_events_guild_on_guild_channel_delete.py
        |   |   |   |-- test_bot_events_guild_on_guild_channel_update.py
        |   |   |   |-- test_bot_events_guild_on_guild_emojis_update.py
        |   |   |   |-- test_bot_events_guild_on_guild_join.py
        |   |   |   |-- test_bot_events_guild_on_guild_remove.py
        |   |   |   |-- test_bot_events_guild_on_guild_role_create.py
        |   |   |   |-- test_bot_events_guild_on_guild_role_delete.py
        |   |   |   |-- test_bot_events_guild_on_guild_role_update.py
        |   |   |   `-- test_bot_events_guild_on_guild_stickers_update.py
        |   |   |-- member
        |   |   |   |-- test_bot_events_member_on_member_join.py
        |   |   |   |-- test_bot_events_member_on_member_remove.py
        |   |   |   |-- test_bot_events_member_on_member_update.py
        |   |   |   `-- test_bot_events_member_on_user_update.py
        |   |   |-- message
        |   |   |   |-- test_bot_events_message_on_message.py
        |   |   |   |-- test_bot_events_message_on_message_delete.py
        |   |   |   |-- test_bot_events_message_on_message_edit.py
        |   |   |   |-- test_bot_events_message_on_raw_reaction_add.py
        |   |   |   |-- test_bot_events_message_on_raw_reaction_remove.py
        |   |   |   |-- test_bot_events_message_on_reaction_add.py
        |   |   |   |-- test_bot_events_message_on_reaction_clear.py
        |   |   |   |-- test_bot_events_message_on_reaction_remove.py
        |   |   |   `-- test_bot_events_message_on_typing.py
        |   |   `-- other
        |   |       |-- test_bot_events_other_on_application_command_error.py
        |   |       |-- test_bot_events_other_on_command.py
        |   |       |-- test_bot_events_other_on_command_error.py
        |   |       |-- test_bot_events_other_on_connect.py
        |   |       |-- test_bot_events_other_on_disconnect.py
        |   |       |-- test_bot_events_other_on_ready.py
        |   |       |-- test_bot_events_other_on_resumed.py
        |   |       |-- test_bot_events_other_on_voice_state_update.py
        |   |       |-- test_bot_events_other_on_wavelink_track_end.py
        |   |       |-- test_bot_events_other_on_wavelink_track_start.py
        |   |       `-- test_bot_events_other_on_webhook_update.py
        |   `-- tasks
        |       `-- test_bot_tasks_database_sync.py
        |-- core
        |   |-- test_core_init.py
        |   |-- test_core_loader.py
        |   |-- test_core_logging.py
        |   |-- test_core_player_state.py
        |   `-- test_core_player_utils.py
        |-- database
        |   |-- models
        |   |   |-- test_database_models_guild.py
        |   |   `-- test_database_models_member.py
        |   |-- repositories
        |   |   |-- test_database_repositories_guild.py
        |   |   `-- test_database_repositories_member.py
        |   |-- test_database_connection.py
        |   `-- test_database_init.py
        |-- helpers
        |   |-- test_helpers_embeds.py
        |   |-- test_helpers_init.py
        |   |-- test_helpers_music_utils.py
        |   `-- test_helpers_permissions.py
        `-- locales
            `-- test_locales_i18n.py

44 directories, 170 files
```