import requests
from telegram import Bot
from datetime import datetime
import asyncio
import xml.etree.ElementTree as ET
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = 7267064983

# 🧠 ترجمة بسيطة (بدون API)
def translate_to_ar(text):
    return text  # نقدر نطورها لاحقاً بـ AI

# 🧠 تلخيص بسيط
def summarize(text):
    return text[:100] + "..." if len(text) > 100 else text

def get_ai_news():
    url = "https://news.google.com/rss/search?q=AI+OpenAI+Claude+technology"
    response = requests.get(url)

    root = ET.fromstring(response.content)
    items = root.findall(".//item")[:5]

    news_text = f"🤖 أخبار الذكاء الاصطناعي - {datetime.now().strftime('%Y-%m-%d')}\n\n"

    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text

        summary = summarize(title)
        translated = translate_to_ar(summary)

        news_text += f"🔹 {translated}\n"
        news_text += f"🕒 {pub_date}\n"
        news_text += f"🔗 {link}\n\n"

    return news_text

async def main():
    bot = Bot(token=TOKEN)

    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=get_ai_news())
            print("✅ AI News sent")
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(86400)

asyncio.run(main())
