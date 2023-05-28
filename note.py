import datetime

class Note:
    __slots__ = 'ident', 'title', 'body', 'create_date', 'modify_date'

    def __init__(self, ident, title, body, create_date=datetime.datetime.today(), modify_date=datetime.datetime.today()):
        self.ident = ident
        self.title = title
        self.body = body
        self.create_date = create_date
        self.modify_date = modify_date

    def modify(self):
        self.modify_date = datetime.datetime.today()

    def __str__(self):
        return f"\n   Id: {self.ident}\n" \
               f"Title: {self.title}\n" \
               f"Create date: {self.create_date}\n" \
               f"Modify date: {self.modify_date}\n" \
               f"Text: {self.body}"

    def to_array(self):
        return [self.ident, self.title, self.body, self.create_date, self.modify_date]