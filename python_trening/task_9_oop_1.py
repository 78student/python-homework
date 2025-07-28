from task_9_checks import Checks

class Input(Checks):

    def __init__(self, loc,text):
        super().__init__(loc)
        self.text=text

search=Input('input#search', 'aaa')
print(search.check_text())

class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Button('button#search', 'bbb')
print(search.check_text())

class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Title('title#search', 'ttt')
print(search.check_text())

class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Link('link#search', 'lll')
print(search.check_text())
