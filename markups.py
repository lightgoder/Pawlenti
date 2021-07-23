from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# --- Menu ---
btnM = KeyboardButton('⬅️ Main menu')

Menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnM)

# --- Main Menu ---
btnLang = KeyboardButton('🔎 Contacts 📞')
btnExch = KeyboardButton('💵 Exchange 💵')
btnRate = KeyboardButton('📊 Exchange rate 📊')
btnRez = KeyboardButton('🏛 Service reserves 🏛')
btnInfo = KeyboardButton('ℹ Information ℹ')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLang, btnRez).add(btnExch, btnRate).add(btnInfo)


# --- Language Menu ---
btnEN = KeyboardButton('English')
btnCN = KeyboardButton('中国人') #китайский юани
btnJP = KeyboardButton('日本語') #японский иены
btnRU = KeyboardButton('Русский')
btnESP = KeyboardButton('Española')
btnKR = KeyboardButton('한국어') #корейский воны
btnMain = KeyboardButton('⬅️ Main menu')

languMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnEN, btnCN, btnJP, btnRU, btnESP, btnKR, btnMain)

# --- Select currency ---
btnUSD = KeyboardButton('USD')
btnCNY = KeyboardButton('CNY') 
btnJPY = KeyboardButton('JPY')
btnRUB = KeyboardButton('RUB')
btnEUR = KeyboardButton('EUR')
btnKRW = KeyboardButton('KRW')
btnMain = KeyboardButton('⬅️ Main menu')

currencyMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnUSD, btnCNY, btnJPY, btnRUB, btnEUR, btnKRW, btnMain)

# --- TRX sum ---
btn2000 = KeyboardButton('2000 Tron(TRX)')
btn2500 = KeyboardButton('2500 Tron(TRX)') 
btn3000 = KeyboardButton('3000 Tron(TRX)')
btn3500 = KeyboardButton('3500 Tron(TRX)')
btn4000 = KeyboardButton('4000 Tron(TRX)')
btn4500 = KeyboardButton('4500 Tron(TRX)')
btn5000 = KeyboardButton('5000 Tron(TRX)')
btn5500 = KeyboardButton('5500 Tron(TRX)')
btn6000 = KeyboardButton('6000 Tron(TRX)')
btnMain = KeyboardButton('⬅️ Main menu')

TRXMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btn2000, btn2500, btn3000, btn3500, btn4000, btn4500, btn5000, btn5500, btn6000)

# --- The next step ---
btnNext = KeyboardButton('The next step ➡️')

nextMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnNext)

# --- Continue ---
btnContinue = KeyboardButton('Continue ➡️')

ContinueMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnContinue)

# --- Final ---
btnFinal = KeyboardButton('I paid ✅')

FinalMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFinal)

# --- Final ---
btnFinal = KeyboardButton('I paid ✅')
btnM = KeyboardButton('⬅️ Main menu')

FinM = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFinal). add(btnM)
