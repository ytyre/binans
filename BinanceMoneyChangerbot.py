from aiogram import Bot, Dispatcher, executor, types
import requests


API_TOKEN = '6235814189:AAFNknDuJUrFmAFMsjsAHVeSjQrFkQO5CEw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['Привет!'])
async def hi(message: types.Message):
    await message.answer('Привет, начнём работу?')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    btn = [
        [
            types.KeyboardButton(text='/Начнём!'),
            types.KeyboardButton(text='/Привет!')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=btn)
    await message.reply("Привет!\nВыбирай кнопку, уважаемый Бибизьян!",
                        reply_markup=keyboard)


@dp.message_handler(commands=['Начнём!'])
async def get_text_messages(message: types.Message):
    btn = [
        [
            types.KeyboardButton(text="/BTC"),
            types.KeyboardButton(text="/USDT"),
            types.KeyboardButton(text="/Ethereum"),
            types.KeyboardButton(text="/BNB")
        ],
    ]
    mar = types.ReplyKeyboardMarkup()
    mar.add(btn)
    keyboard = types.ReplyKeyboardMarkup(keyboard=btn)
    await message.reply("Выбирай монету, Монкей!",
                        reply_markup=keyboard)


@dp.message_handler(commands=['BTC'])
async def Bitcoins(message: types.Message):
    url = 'https://data.binance.com/api/v3/avgPrice'
    param = {'symbol': 'BTCUSDT'}
    get_info = requests.get(url, params=param)
    item = get_info.json()
    price = float(item["price"])
    if get_info.status_code == 200:
        await message.reply(f'Цена "Bitcoin" на данный момент состовляет {price:.2f}$')
    else:
        print('Произошла ошибка при получении информации в json.')


@dp.message_handler(commands=['BNB'])
async def Bitcoins(message: types.Message):
    url = 'https://data.binance.com/api/v3/avgPrice'
    param = {'symbol': 'BNBUSDT'}
    get_info = requests.get(url, params=param)
    item = get_info.json()
    price = float(item["price"])
    if get_info.status_code == 200:
        await message.reply(f'Цена "BNB" на данный момент состовляет {price:.2f}$')
    else:
        print('Произошла ошибка при получении информации в json.')


@dp.message_handler(commands=['Ethereum'])
async def Bitcoins(message: types.Message):
    url = 'https://data.binance.com/api/v3/avgPrice'
    param = {'symbol': 'ETHUSDT'}
    get_info = requests.get(url, params=param)
    item = get_info.json()
    price = float(item["price"])
    if get_info.status_code == 200:
        await message.reply(f'Цена "Ethereum" на данный момент состовляет {price:.2f}$')
    else:
        print('Произошла ошибка при получении информации в json.')


@dp.message_handler(commands=['USDT'])
async def Bitcoins(message: types.Message):
    url = 'https://data.binance.com/api/v3/avgPrice'
    param = {'symbol': 'USDCUSDT'}
    get_info = requests.get(url, params=param)
    item = get_info.json()
    price = float(item["price"])
    if get_info.status_code == 200:
        await message.reply(f'Цена "USDT" на данный момент состовляет {price:.2f}$')
    else:
        print('Произошла ошибка при получении информации в json.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
