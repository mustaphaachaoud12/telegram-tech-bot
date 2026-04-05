import requests
from telegram import Bot
from datetime import datetime
import asyncio
import xml.etree.ElementTree as ET
import os

# 🔐 ناخدو التوكن من Render (ماشي من الكود)
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = 7267064983

def get_tech_news():
    try:
        url = "https://news.google.com/rss/search?q=technology"
        response = requests.get(url)

        root = ET.fromstring(response.content)
        items = root.findall(".//item")[:5]

        news_text = f"📰 Tech News - {datetime.now().strftime('%Y-%m-%d')}\n\n"

        for item in items:
            title = item.find("title").text
            link = item.find("link").text
            news_text += f"🔹 {title}\n{link}\n\n"

        return news_text

    except:
        return "❌ وقع مشكل فـ جلب الأخبار"

async def main():
    bot = Bot(token=TOKEN)

    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=get_tech_news())
            print("✅ News sent")
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(86400)  # 24h

# تشغيل البوت
asyncio.run(main())
