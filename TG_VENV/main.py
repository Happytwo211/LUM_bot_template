
import telebot
from telebot import types

TOKEN = '///token'
bot = telebot.TeleBot(TOKEN)
admin_id = [816710725]

inline_kb_st = types.InlineKeyboardMarkup(row_width=2)
inline_bt_1 = types.InlineKeyboardButton('Запустить "ЛюМ"', 'https://www.wikipedia.org')
inline_bt_2 = types.InlineKeyboardButton('Московская Афиша', 'https://www.afisha.ru')
inline_bt_3 = types.InlineKeyboardButton('Cтать частичкой ЛЮМ', 'https://t.me/lum_moscow')
inline_bt_4 = types.InlineKeyboardButton(text="О нас!",
                                         callback_data='about_us')
inline_kb_st.add(inline_bt_1).add(inline_bt_2).add(inline_bt_3).add(inline_bt_4)

keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                               input_field_placeholder='"ЛюМ"- Люблю Москву!',
                                                   one_time_keyboard=True)
button1 = types.KeyboardButton('Кнопка 1')
button2 = types.KeyboardButton('Кнопка 2')
button3 = types.KeyboardButton('Кнопка 3')

keyboard_start.add(button1, button2, button3)  # Кнопки по вертикали
# keyboard.add(button1).add(button2).add(button3) #.add(button4).add(button5) #Кнопки по шиирине



class CommandStart:

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_photo(message.chat.id, 'https://imgur.com/a/0IQeUYB',
                       f'Добро пожалосвать, {message.chat.username}!'
                       f'\n'
                       f'\nЭто бот проекта "ЛюМ" - Люблю Москву!'
                       f'\n'
                       f'\nАудио-Гид для самостоятельных интерактивных экскурсий по Москве для всей семьи!', reply_markup=inline_kb_st)


        bot.send_message(message.chat.id, f'Или нажми на кнопку', reply_markup=keyboard_start, disable_notification=True)


class AdmPanel:
    @bot.message_handler(commands=['adm'])
    def amd_panel(message):
        if message.from_user.id in admin_id:
            amd_kb = types.InlineKeyboardMarkup(row_width=2)
            amd_b1 = types.InlineKeyboardButton('Админская функция 1', callback_data='adm1')
            amd_b2 = types.InlineKeyboardButton('Админская функция 2', callback_data='amd2')
            amd_b3 = types.InlineKeyboardButton('Админская функция 3', callback_data='adm3')
            amd_kb.add(amd_b1).add(amd_b2).add(amd_b3)
            bot.send_message(message.chat.id, f'Вы вошли в админскую панель', reply_markup=amd_kb)

        else:
            bot.send_message(message.chat.id, f'У вас нет доступа к админ-панели')





class InlineKeyboard:

    @bot.callback_query_handler(func=lambda call: call.data == 'main_page')
    def start_lum(call):
        message = call.message
        bot.send_photo(message.chat.id, 'https://imgur.com/a/0IQeUYB',
                       f'Добро пожалосвать, {message.chat.username}!'
                       f'\n'
                       f'\nЭто бот проекта "ЛюМ" - Люблю Москву!'
                       f'\n'
                       f'\nАудио-Гид для самостоятельных интерактивных экскурсий по Москве для всей семьи!',
                       reply_markup=inline_kb_st)

    @bot.callback_query_handler(func=lambda call: call.data == 'about_us')
    def start_lum(call):
        inline_social_media_kb = types.InlineKeyboardMarkup(row_width=3)
        vk_button = types.InlineKeyboardButton('VK', 'https://vk.com')
        tg_button = types.InlineKeyboardButton('TG', 'https://weba.telegram.org/')
        inst_button = types.InlineKeyboardButton('INSTA', 'https://instagram.com/')
        main_page_b = types.InlineKeyboardButton(text='На главную!', callback_data='main_page')
        inline_social_media_kb.add(vk_button).add(tg_button).add(inst_button).add(main_page_b)
        message = call.message
        bot.send_message(message.chat.id, f'Наша комманда:'
                         ,reply_markup=inline_social_media_kb)

    @bot.callback_query_handler(func=lambda call: call.data == 'adm1')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 1')

    @bot.callback_query_handler(func=lambda call: call.data == 'amd2')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 2')

    @bot.callback_query_handler(func=lambda call: call.data == 'adm3')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 3')


class NotHandle:

    @bot.message_handler(content_types=['video', 'audio', 'sticker', 'photo', 'document', 'contact', 'emoji'])
    def handle_content_types(message):
        bot.send_message(message.chat.id, f'Бот такое не понимает'

                         f'\nВот список доступных комманд:', reply_markup=inline_kb_st)


class ReplyButtons:

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):

        if message.text == 'Кнопка 1':
            bot.send_message(message.chat.id, f'Вы нажали кнопку 1', reply_markup=keyboard_start)

        elif message.text == 'Кнопка 2':
            bot.send_message(message.chat.id, f'Вы нажали кнопку 2', reply_markup=keyboard_start)

        elif message.text == 'Кнопка 3':
            bot.send_message(message.chat.id, f'Вы нажали кнопку 3', reply_markup=keyboard_start)


        else:
            bot.send_message(message.chat.id, f'Такой комманды нет'
                                              f'\nСписок доступных комманд',
                             reply_markup=inline_kb_st)




bot.infinity_polling()
