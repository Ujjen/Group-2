
class Article:

    def __init__(self, title, source, date, *args, **kwargs):
        self.title = title
        self.source = source
        self.date = date

    def setTitle(self, title):
        self.title = title

    def setSource(self, source):
        self.source = source

    def setDate(self, date):
        self.date = date

    def getTitle(self):
        return self.title

    def getSource(self):
        return self.source

    def getDate(self):
        return self.date