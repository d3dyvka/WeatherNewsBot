from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from utils.utils import get_weather_info
from utils.utils import get_joke_pls
from utils.utils import get_news
from decouple import config

start_Router = Router()

@start_Router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("приветсвую тебя в этом боте!\nнапиши /help для просмотра всех команд!")

@start_Router.message(Command('help'))
async def message_handler(message: types.Message):
    await message.answer("Вот основные команды бота:\n/start - запуск бота\n/help - справка о всех командах\n"
                         "/echo - бот ответит вам вашим же сообщением\n/weather - вывод погоды в Новосибирске\n"
                         "/news - выводит новости по заданной теме\n/joke - рандомная смешная шутка специально для вас")

@start_Router.message(Command('echo'))
async def echo_message(message: types.Message, command: CommandObject):
    to_echo = command.args
    if not to_echo:
        await message.answer("Для повторения вашего сообщения нужно ввести команду в формате: /echo [сообщение]\n"
                             "например: /echo Привет!")
        return
    await message.answer(to_echo)

@start_Router.message(Command('weather'))
async def get_weather(message: types.Message):
    weather = await get_weather_info(config('CityName'), config('WeatherKey'))
    await message.answer(weather)

@start_Router.message(Command('joke'))
async def get_joke(message: types.Message):
    joke = await get_joke_pls()
    await message.answer(joke)

@start_Router.message(Command('news'))
async def news(message: types.Message, command: CommandObject):
    topic = command.args
    if not topic:
        await message.answer("Для получения новостей нужно ввести сообщение в формате /news [тема]\n"
                             "например: /news технологии")
        return
    News = await get_news(config('NewsKey'), topic)
    for i in News:
        await message.answer(i)