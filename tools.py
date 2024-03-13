import json 

class Tools:
    # Загрузка настроек из файла
    def load_config():
        with open('settings.json', 'r') as file:
            return json.load(file)
        
    # Загрузка ответов бота
    def load_replies():
        with open('bot_replies.json', 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def read_html(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()