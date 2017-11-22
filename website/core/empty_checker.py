from html.parser import HTMLParser


class EMPTYChecker(HTMLParser):
    def __init__(self):
        self.is_empty = True
        super(EMPTYChecker, self).__init__()

    def handle_data(self, data):
        if data.strip():
            self.is_empty = False

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self.is_empty = False