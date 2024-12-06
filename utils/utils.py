import aiohttp

async def get_weather_info(city: str, api_key: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                return (
                    f"погода в {city}е\n"
                    f"температура на улице: {round(temp)}°C\n"
                    f"ощущается как: {round(feels_like)}°C"
                )
            else:
                return "Не удалось получить данные о погоде. Попробуйте позже"

async def get_joke_pls():
    url = "https://official-joke-api.appspot.com/random_joke"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                joke = data['setup']
                punchline = data['punchline']
                return joke + "\n" + punchline
            else:
                return "Не удалось найти шутку, попробуйте позже"

async def get_news(api: str, topic: str):
    url = f"https://newsdata.io/api/1/news?apikey={api}&language=ru&q={topic}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                articles = data.get("results", [])
                if articles:
                    news_messages = []
                    for article in articles[:5]:
                        title = article.get("title", "Без названия")
                        link = article.get("link", "Ссылка недоступна")
                        news_messages.append(f"{title}\nПодробнее:{link}")

                    return news_messages
                else:
                    return "По вашей теме ничего не найдено"
            else:
                return "Не удалось получить новости. Попробуйте позже"
