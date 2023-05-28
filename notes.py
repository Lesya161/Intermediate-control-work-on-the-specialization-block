import logger
from note import Note


class Notes:
    notes: [Note] = []
    count: int = 0
    notes_store = ''
    logger = logger.get_logger(__name__)

    def __init__(self, notes_store):
        self.notes_store = notes_store
        for x in self.notes_store.read_all():
            self.notes.append(Note(x[0], x[1], x[2], x[3], x[4]))
            if int(x[0]) > self.count:
                self.count = int(x[0])

    def add_note(self, title, body):
        self.count += 1
        self.notes.append(Note(str(self.count), title, body))
        self.logger.info(f"Заметка {self.count} добавлена.")
        self.save()

    def save(self):
        self.logger.info("Сохранение заметок в файл.")
        all_notes = []
        for x in self.notes:
            all_notes.append(x.to_array())
        self.notes_store.save_all(all_notes)

    def get_titles(self):
        all_titles = []
        for x in self.notes:
            all_titles.append([x.ident, x.title])
        return all_titles

    def find_index(self, ident):
        for i in range(len(self.notes)):
            if self.notes[i].ident == ident:
                self.logger.info(f"Заметка {ident} найдена.")
                return i
        self.logger.info(f"Заметка {ident} не найдена.")
        return -1

    def del_note(self, ident):
        i = self.find_index(ident)
        if i != -1:
            self.notes.pop(i)
            self.save()
            self.logger.info(f"Заметка {ident} удалена.")
            return 'Note deleted.'
        else:
            return 'Not found.'

    def read_note(self, ident):
        i = self.find_index(ident)
        if i != -1:
            self.logger.info(f"Заметка {ident} прочитана.")
            return self.notes[i]
        return 'Not found.'

    def edit_note(self, ident, title, body):
        i = self.find_index(ident)
        if i != -1:
            self.notes[i].title = title
            self.notes[i].body = body
            self.notes[i].modify()
            self.logger.info(f"Заметка {ident} отредактирована.")
            self.save()