# Состояние, в котором находится пользователь
class BotState:
    START = "start"
    MESSAGE = "message"
    CLEAR = "clear"
    SYSTEM = "system"
    SYSTEM_STEP2 = "system_step2"
    ANSWER = "answer"
    MODEL = "model"
    MODE = "mode"
    VOICE = "voice"
    VOICE_STEP2 = "voice_step2"
    RECOGNITION = "recognition"
    RECOGNITION_STEP2 = "recognition_step2"
    RECOGNITION_STEP3 = "recognition_step3"


# Формат ответа
class BotAnswer:
    TEXT = ("Текст", "text")
    VOICE = ("Голос", "voice")
    ALL = ("Все", "all")


# Режим работы бота, его функционал
class BotMode:
    ECHO = ("Эхобот", "echo")
    AI = ("Искусственный интеллект", "ai")
    TRANSLATE = ("Переводчик", "translate")


# Используемая модель ИИ
class BotAIModel:
    CHAT_GPT_35 = ("GPT-3.5 Turbo 16K", "gpt-3.5-turbo-1106")
    CHAT_GPT_4 = ("GPT-4 Turbo 128K", "gpt-4-1106-preview")
    DALLE3 = ("DALL-E 3", "dall-e-3")


# Настройка типа перевода
class BotTypeTranslate:
    AUTO = ("Авто", "auto")
    MANUAL = ("Вручную", "manual")


class BotParams:
    def __init__(self):
        self.state = BotState.START
        self.answer = BotAnswer.TEXT
        self.mode = BotMode.AI
        self.model = BotAIModel.CHAT_GPT_35
        self.type_translate = BotTypeTranslate.AUTO
        self.data = {}
        self.reset_data()

    def reset_data(self):
        self.data = {"text": "", "file_id": None, "last_time": None}


def get_class_values(cls):
    class_values = [getattr(cls, attr) for attr in vars(cls) if not attr.startswith("__")]
    return class_values


def get_class_dict(cls):
    values = get_class_values(cls)
    if values and isinstance(values[0], str):
        merged_dict = {item.strip().capitalize(): item for item in values}
    else:
        merged_dict = {item[0]: item for item in values}
    return merged_dict


def is_value_in_class_values(value, cls):
    return value in get_class_values(cls)
