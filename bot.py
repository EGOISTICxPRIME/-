from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

print("""
╔══════════════════════════════╗
        🎧 𝐀ʏᴜᴜ 𝐌ᴜꜱɪᴄ 🎧
╚══════════════════════════════╝

⚡ 𝟐𝟒/𝟕 𝐓ᴇʟᴇɢʀᴀᴍ 𝐌ᴜꜱɪᴄ 𝐁ᴏᴛ
💗 𝐒ᴍᴏᴏᴛʜ • 𝐂ʟᴇᴀɴ • 𝐀ᴅ-𝐅ʀᴇᴇ
🎶 𝐋ɪᴍɪᴛʟᴇꜱꜱ 𝐒ᴛʀᴇᴀᴍɪɴɢ 𝐕ɪʙᴇꜱ
🚀 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ @AYUXUPDATES 

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🥂 𝐁ᴀʙʏ 𝐀ʟɪᴠᴇ 💗
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
app = Client(
    "AYU_MUSIC",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

app.run()