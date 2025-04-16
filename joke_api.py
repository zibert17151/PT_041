import aiohttp
import random

with open("jokes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    random_text = random.choice(lines).strip()
print(random_text)

async def get_joke(category="Any", blacklist="", JOKE_API_URL=""):

    params = {
        "type": "twopart",
        "category": category,
        "blacklistFlags": blacklist
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(JOKE_API_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if "setup" in data and "delivery" in data:
                    return f"😂 {data['setup']}\n🤔 {data['delivery']}"
                elif "joke" in data:
                    return f"🤣 {data['joke']}"
                else:
                    return "❌ Не удалось получить шутку."
            else:
                return "⚠️ Ошибка запроса к API."