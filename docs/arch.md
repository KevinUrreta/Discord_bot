```
# tree -I "venv|__pycache__|postgres_data"
.
├── docker
|   ├── docker-compose.yml
|   └── dockerfile
├── docs
|   └── arch.md
├── lavalink
|   ├── application.yml
|   ├── application.yml.backup
|   ├── dockerfile
|   └── plugins
|       ├── lavasrc-plugin-4.8.3.jar
|       └── youtube-plugin-1.18.2.jar
├── logs
|   ├── bot.log
|   └── lavalink.log
├── main.py
├── requirements.txt
├── src
|   ├── bot
|   |   ├── commands
|   |   |   ├── moderation
|   |   |   |   └── cls.py
|   |   |   └── music
|   |   |       ├── clear.py
|   |   |       ├── join.py
|   |   |       ├── leave.py
|   |   |       ├── loop.py
|   |   |       ├── lyrics.py
|   |   |       ├── pause.py
|   |   |       ├── play.py
|   |   |       ├── queue.py
|   |   |       ├── remove.py
|   |   |       ├── resume.py
|   |   |       ├── shuffle.py
|   |   |       ├── skip.py
|   |   |       ├── stop.py
|   |   |       └── volume.py
|   |   └── events
|   |       ├── guild
|   |       |   ├── on_guild_channel_create.py
|   |       |   ├── on_guild_channel_delete.py
|   |       |   ├── on_guild_channel_update.py
|   |       |   ├── on_guild_emojis_update.py
|   |       |   ├── on_guild_role_create.py
|   |       |   ├── on_guild_role_delete.py
|   |       |   ├── on_guild_role_update.py
|   |       |   └── on_guild_stickers_update.py
|   |       ├── member
|   |       |   ├── on_member_join.py
|   |       |   ├── on_member_remove.py
|   |       |   ├── on_member_update.py
|   |       |   └── on_user_update.py
|   |       ├── message
|   |       |   ├── on_message.py
|   |       |   ├── on_message_delete.py
|   |       |   ├── on_message_edit.py
|   |       |   ├── on_raw_reaction_add.py
|   |       |   ├── on_raw_reaction_remove.py
|   |       |   ├── on_reaction_add.py
|   |       |   ├── on_reaction_clear.py
|   |       |   ├── on_reaction_remove.py
|   |       |   └── on_typing.py
|   |       └── other
|   |           ├── on_command.py
|   |           ├── on_command_error.py
|   |           ├── on_connect.py
|   |           ├── on_disconnect.py
|   |           ├── on_ready.py
|   |           ├── on_resumed.py
|   |           ├── on_voice_state_update.py
|   |           ├── on_wavelink_track_end.py
|   |           └── on_webhook_update.py
|   ├── core
|   |   ├── loader.py
|   |   └── logging.py
|   ├── database
|   |   ├── __init__.py
|   |   ├── connection.py
|   |   ├── models
|   |   |   └── guild.py
|   |   └── repositories
|   |       └── guild.py
|   └── locales
|       ├── de_DE.json
|       ├── en_US.json
|       ├── es_ES.json
|       ├── fr_FR.json
|       ├── i18n.py
|       ├── it_IT.json
|       ├── ja_JP.json
|       ├── nl_NL.json
|       ├── pl_PL.json
|       └── pt_PT.json
└── tests
    ├── src
    |   └── bot
    |       ├── commands
    |       |   └── music.py
    |       └── events
    |           └── events.py
    └── test_music.py

26 directories, 76 files
```
