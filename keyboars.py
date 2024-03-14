from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    def main_menu(self):
        keyboard = [
            [InlineKeyboardButton("Найти по частям тела 🔍", callback_data='find_by_body_part')],
            [InlineKeyboardButton("Самые частые проблемы ❗️", callback_data='common_issues')]
        ]
        return InlineKeyboardMarkup(keyboard)

    def back_to_main(self):
        keyboard = [
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_main')]
        ]
        return InlineKeyboardMarkup(keyboard)

    def body_parts(self):
        keyboard = [
            [InlineKeyboardButton("Голова 👦🏼", callback_data='head')],
            [InlineKeyboardButton("Горло 🗣", callback_data='throat')],
            [InlineKeyboardButton("Спина 🧎🏼‍♂️", callback_data='back')],
            [InlineKeyboardButton("Желудок 🍐", callback_data='stomach')],
            [InlineKeyboardButton("Кишечник", callback_data='intestines')],
            [InlineKeyboardButton("Сердце 🫀", callback_data='heart')],
            [InlineKeyboardButton("Лёгкие 🫁", callback_data='lungs')],
            [InlineKeyboardButton("Почки 🚻", callback_data='kidneys')],
            [InlineKeyboardButton("Глаза 👁", callback_data='eyes')],
            [InlineKeyboardButton("Зубы 🦷", callback_data='teeth')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_main')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def common_issues(self):
        keyboard = [
            [InlineKeyboardButton("Ушиб 🩹", callback_data='bruise')],
            [InlineKeyboardButton("Вывех 🦴", callback_data='dislocation')],
            [InlineKeyboardButton("Перелом 🩻", callback_data='fracture')],
            [InlineKeyboardButton("Кровотечение 🩸", callback_data='bleeding')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_main')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def head(self):
        keyboard = [
            [InlineKeyboardButton("Сотрясение мозга", callback_data='concussion')],
            [InlineKeyboardButton("Перелом черепа", callback_data='skull_fracture')],
            [InlineKeyboardButton("Мигрень", callback_data='migrane')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def throat(self):
        keyboard = [
            [InlineKeyboardButton("Ангионевротический отек", callback_data='throat_swelling')],
            [InlineKeyboardButton("Острое затруднение дыхания", callback_data='difficulty_breathing')],
            [InlineKeyboardButton("Асфиксия", callback_data='asphyxia')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def back(self):
        keyboard = [
            [InlineKeyboardButton("Травма позвоночка", callback_data='spinal_injury')],
            [InlineKeyboardButton("Острый межпозвоночный грыжевой пролапс", callback_data='acute_intervertebral_herniated_prolapse')],
            [InlineKeyboardButton("Каудальный синдром", callback_data='cauda_equina_syndrome')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def stomach(self):
        keyboard = [
            [InlineKeyboardButton("Перфорация желудка", callback_data='gastric_perforation')],
            [InlineKeyboardButton("Острый аппендицит", callback_data='acute_appendicitis')],
            [InlineKeyboardButton("Гастроинтестинальное кровотечение", callback_data='gastrointestinal_bleeding')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def intestines(self):
        keyboard = [
            [InlineKeyboardButton("Инвагинация кишечника", callback_data='intestinal_intussusception')],
            [InlineKeyboardButton("Острая кишечная непроходимость", callback_data='acute_intestinal_obstruction')],
            [InlineKeyboardButton("Ишемический колит", callback_data='ischemic_colitis')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def heart(self):
        keyboard = [
            [InlineKeyboardButton("Инфаркт миокарда", callback_data='myocardial_infarction')],
            [InlineKeyboardButton("Остановка сердца", callback_data='cardiac_arrest')],
            [InlineKeyboardButton("Тромбоэмболия легочной артерии", callback_data='pulmonary_embolism')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)

    def kidneys(self):
        keyboard = [
            [InlineKeyboardButton("Острая почечная недостаточность", callback_data='acute_renal_failure')],
            [InlineKeyboardButton("Почечная колика", callback_data='renal_colic')],
            [InlineKeyboardButton("Гидронефроз", callback_data='hydronephrosis')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)

    def lungs(self):
        keyboard = [
            [InlineKeyboardButton("Пневмоторакс", callback_data='pneumothorax')],
            [InlineKeyboardButton("Отек легких", callback_data='pulmonary_edema')],
            [InlineKeyboardButton("Тромбоэмболия легочной артерии", callback_data='pulmonary_embolism')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)

    def eyes(self):
        keyboard = [
            [InlineKeyboardButton("Отслойка сетчатки", callback_data='retinal_detachment')],
            [InlineKeyboardButton("Глаукоматозный криз", callback_data='glaucomatous_crisis')],
            [InlineKeyboardButton("Химический ожог глаза", callback_data='chemical_eye_burn')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def teeth(self):
        keyboard = [
            [InlineKeyboardButton("Абсцесс зуба", callback_data='tooth_abscess')],
            [InlineKeyboardButton("Остеомиелит челюсти", callback_data='osteomyelitis')],
            [InlineKeyboardButton("Тяжелая травма челюсти", callback_data='bad_jaw_injury')],
            [InlineKeyboardButton("Назад ⬅️", callback_data='back_to_body_parts')]
        ]
        return InlineKeyboardMarkup(keyboard)


