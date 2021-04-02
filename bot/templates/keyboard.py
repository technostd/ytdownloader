class Action:
    TYPE_TEXT = 'text'
    TYPE_OPEN_LINK = 'open_link'
    TYPE_LOCATION = 'location'
    TYPE_VK_PAY = 'vkpay'
    TYPE_VK_APPS = 'open_app'
    TYPE_CALLBACK = 'callback'

    def __init__(self, type: str = TYPE_TEXT, payload=None, **kwargs):


class Button:
    COLOR_PRIMARY = 'primary'
    COLOR_SECONDARY = 'secondary'
    COLOR_NEGATIVE = 'negative'
    COLOR_POSITIVE = 'positive'

    def __init__(self, action: Action, color=COLOR_PRIMARY):
        self.action = action
        self.color = color


class Keyboard:

    def __init__(self, inline: bool = False, one_time: bool = False):
        self.keyboard = {
            'inline': inline,
            'one_time': one_time,
            'buttons': [[]]
        }
