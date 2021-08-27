import os
from Group_Music_Probot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL

class Messages():
      START_MSG = """
Hey, I'm Katarina 🎵
I can play music in your group's voice call. 
Add me to your group and play music freely!

Try the /help Command below to know my abilities.
"""
      
      HELP_MSG = [
        ".",
f"""
Hey, I'm Katarina 🎵
I can play music in your group's voice call. 
Add me to your group and play music freely!

Try the /help Command below to know my abilities.
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @KatarinaMusixUserbot to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Commands**

**=>> Song Playing 🎧**

- /p: Play the requestd song
- /p [yt url] : Play the given yt url
- /p [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /s: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /pl: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite Assistant to your chat.
"""
      ]
