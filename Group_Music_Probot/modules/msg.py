import os
from Group_Music_Probot.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL

class Messages():
      START_MSG = """
Hey, I'm **Nezuko**. I'm Music Bot for Truthful Demons. Nice to meet you!
Unfortunately, this bot is exclusive for Truthful Demons.
"""
      
      HELP_MSG = [
        ".",
f"""
Hey, I'm **Nezuko**. I'm Music Bot for Truthful Demons. Nice to meet you!
Unfortunately, this bot is exclusive for Truthful Demons.
""",

f"""
**Commands**

**=>> Song Playing 🎧**

- /p: Play the requestd song
- /p [yt url] : Play the given yt url
- /p [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /s: Skips the current track (unstable command)
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
