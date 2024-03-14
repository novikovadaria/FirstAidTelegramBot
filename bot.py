from telegram import ParseMode
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from keyboars import Keyboard
from tools import Tools

KEYBOARD = Keyboard()

class Bot:
    def __init__(self, config, bot_replies, issues):
        self.config = config
        self.bot_replies = bot_replies
        self.issues = issues

    def init(self):
        # Использование токена из файла настроек
        updater = Updater(self.config['token'], use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('start', self.start))
        dp.add_handler(CallbackQueryHandler(self.button))

        # Начинаем поиск обновлений
        updater.start_polling()
        updater.idle()

    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(text=self.bot_replies['hello_message'], reply_markup=KEYBOARD.main_menu()
)

    def button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()

        # Обработка основных кнопок и частей тела через словарь
        main_actions = {
            'find_by_body_part': lambda: query.edit_message_text(text=self.bot_replies['find_by_body_part'], reply_markup=KEYBOARD.body_parts()),
            'common_issues': lambda: query.edit_message_text(text=self.bot_replies['common_issues'], reply_markup=KEYBOARD.common_issues()),
            'back_to_main': lambda: query.edit_message_text(text=self.bot_replies['hello_message'], reply_markup=KEYBOARD.main_menu()),
            'back_to_body_parts': lambda: query.edit_message_text(text=self.bot_replies['hello_message'], reply_markup=KEYBOARD.body_parts()),
            'head': lambda: query.edit_message_text(text=self.bot_replies['head'], reply_markup=KEYBOARD.head()),
            'throat': lambda: query.edit_message_text(text=self.bot_replies['throat'], reply_markup=KEYBOARD.throat()),
            'stomach': lambda: query.edit_message_text(text=self.bot_replies['stomach'], reply_markup=KEYBOARD.stomach()),
            'intestines': lambda: query.edit_message_text(text=self.bot_replies['intestines'], reply_markup=KEYBOARD.intestines()),
            'heart': lambda: query.edit_message_text(text=self.bot_replies['heart'], reply_markup=KEYBOARD.heart()),
            'kidneys': lambda: query.edit_message_text(text=self.bot_replies['kidneys'], reply_markup=KEYBOARD.kidneys()),
            'lungs': lambda: query.edit_message_text(text=self.bot_replies['lungs'], reply_markup=KEYBOARD.lungs()),
            'eyes': lambda: query.edit_message_text(text=self.bot_replies['eyes'], reply_markup=KEYBOARD.eyes()),
            'teeth': lambda: query.edit_message_text(text=self.bot_replies['teeth'], reply_markup=KEYBOARD.teeth()),
            'head': lambda: query.edit_message_text(text=self.bot_replies['head'], reply_markup=KEYBOARD.head())
        }

        # Обработка специфических запросов по здоровью через единый подход
        health_issues = [
            'concussion','skull_fracture','migrane', #ГОЛОВА
            'throat_swelling', 'difficulty_breathing', 'asphyxia', #ГОРЛО
            'spinal_injury','acute_intervertebral_herniated_prolapse','cauda_equina_syndrome', #СПИНА
            'gastric_perforation','acute_appendicitis','gastrointestinal_bleeding', #ЖЕЛУДОК
            'intestinal_intussusception', 'acute_intestinal_obstruction','ischemic_colitis', #КИШЕЧНИК
            'myocardial_infarction','cardiac_arrest','pulmonary_embolism', #СЕРДЦЕ
            'acute_renal_failure','renal_colic','hydronephrosis', #ПОЧКИ
            'pneumothorax', 'pulmonary_edema', #ЛЕГКИЕ
            'retinal_detachment','glaucomatous_crisis','chemical_eye_burn', #ГЛАЗА
            'tooth_abscess','osteomyelitis','bad_jaw_injury', #ЗУБЫ
            'bruise', 'dislocation', 'fracture', 'bleeding' #ЧАСТЫЕ ПРОБЛЕМЫ
            ]

        if query.data in main_actions:
            main_actions[query.data]()
        elif query.data in health_issues:
            query.edit_message_text(text=Tools.read_html(f"{self.issues}/{query.data}.html"), parse_mode=ParseMode.HTML, reply_markup=KEYBOARD.back_to_main())