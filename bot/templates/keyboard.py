import json


class VkActionType:
    """ VK keyboard button available actions: const """

    TYPE_TEXT = 'text'
    TYPE_OPEN_LINK = 'open_link'
    TYPE_LOCATION = 'location'
    TYPE_VK_PAY = 'vkpay'
    TYPE_VK_APPS = 'open_app'
    TYPE_CALLBACK = 'callback'


class VkButtonColor:
    """ VK keyboard available colors: const """

    COLOR_PRIMARY = 'primary'
    COLOR_SECONDARY = 'secondary'
    COLOR_NEGATIVE = 'negative'
    COLOR_POSITIVE = 'positive'


class VkButtonAction:
    """ Action type and parameters description """

    def __init__(self,
                 type: str = VkActionType.TYPE_TEXT,
                 label: str = None,
                 link: str = None,
                 hash: str = None,
                 app_id: int = None,
                 owner_id: int = None,
                 payload: str = None):
        """
        Basic constructor for VK button action

        :param type: Type
        :type type: str

        :param label: Label
        :type label: str

        :param link: Link
        :type link: str

        :param hash: Hash
        :type hash: str

        :param app_id: VK app ID
        :type app_id: int

        :param owner_id: Owner ID
        :type owner_id: int

        :param payload: Payload
        :type payload: str

        :except UndefinedTypeException: Action type not in available type list
        """

        if type not in [VkActionType.TYPE_TEXT,
                        VkActionType.TYPE_OPEN_LINK,
                        VkActionType.TYPE_LOCATION,
                        VkActionType.TYPE_VK_PAY,
                        VkActionType.TYPE_VK_APPS,
                        VkActionType.TYPE_CALLBACK]:
            raise Exception('UndefinedTypeException')
        self.type = type
        self.label = label
        self.link = link
        self.hash = hash
        self.app_id = app_id
        self.owner_id = owner_id
        self.payload = payload

    def __dict__(self):
        result = {
            'type': self.type,
            'label': self.label,
            'link': self.link,
            'hash': self.hash,
            'app_id': self.app_id,
            'owner_id': self.owner_id,
            'payload': self.payload
        }

        to_del = []
        for key in result:
            if result[key] is None:
                to_del.append(key)

        for key in to_del:
            result.__delitem__(key)

        return result


class VkButton:
    """ VK keyboard button color and action description """

    def __init__(self, action: VkButtonAction, color=VkButtonColor.COLOR_PRIMARY):
        self.action = action
        self.color = color

    @staticmethod
    def text(label: str, payload: str = None, color: str = VkButtonColor.COLOR_PRIMARY):
        return VkButton(action=VkButtonAction(type=VkActionType.TYPE_TEXT, label=label, payload=payload), color=color)

    def __dict__(self):
        result = {
            'action': self.action.__dict__(),
            'color': self.color
        }

        to_del = []
        for key in result:
            if result[key] is None:
                to_del.append(key)

        for key in to_del:
            result.__delitem__(key)

        return result


class VkKeyboard:
    """ VK keyboard buttons and options description """

    MAX_BUTTONS_ON_LINE = 5
    MAX_DEFAULT_LINES = 10
    MAX_INLINE_LINES = 6

    def __init__(self, inline: bool = False, one_time: bool = False):
        self.inline = inline
        self.one_time = one_time
        self.buttons = []

    def add_button(self, button: VkButton):
        if len(self.buttons[1::-1]) >= self.MAX_BUTTONS_ON_LINE:
            raise Exception('Too much buttons in line')
        self.buttons[1::-1].append(button.__dict__())

    def add_line(self, line: list):
        if (len(self.buttons) >= self.MAX_DEFAULT_LINES and not self.inline) or (
                len(self.buttons) >= self.MAX_INLINE_LINES and self.inline):
            raise Exception('Too much lines in keyboard')
        for button in line:
            if button is not VkButton:
                raise Exception('NotButtonException')
        self.buttons.append(line)

    def clear(self):
        self.buttons.clear()

    def __str__(self):
        return json.loads(self.json())

    def json(self):
        return json.dumps(self.__dict__())

    def __dict__(self):
        return {
            'one_time': self.one_time,
            'buttons': self.buttons,
            'inline': self.inline
        }
