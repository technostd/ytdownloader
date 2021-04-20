class Action:
    TYPE_TEXT = 'text'
    TYPE_OPEN_LINK = 'open_link'
    TYPE_LOCATION = 'location'
    TYPE_VK_PAY = 'vkpay'
    TYPE_VK_APPS = 'open_app'
    TYPE_CALLBACK = 'callback'

    def __init__(self,
                 type: str = TYPE_TEXT,
                 label: str = None,
                 link: str = None,
                 hash: str = None,
                 app_id: int = None,
                 owner_id: int = None,
                 payload=None):
        if type not in [self.TYPE_TEXT,
                        self.TYPE_OPEN_LINK,
                        self.TYPE_LOCATION,
                        self.TYPE_VK_PAY,
                        self.TYPE_VK_APPS,
                        self.TYPE_CALLBACK]:
            raise Exception('UndefinedTypeException')
        self.type = type
        self.label = label
        self.link = link
        self.hash = hash
        self.app_id = app_id
        self.owner_id = owner_id
        self.payload = payload

    def __dict__(self):
        pass


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
