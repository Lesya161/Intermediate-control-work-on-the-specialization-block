
import logger
import view
from notes import Notes
from store import Store

logger = logger.get_logger(__name__)

if __name__ == '__main__':
    logger.info("Начинаем")
    filename = 'notes.csv'
    notes_store = Store(filename)
    notes = Notes(notes_store)
    logger.info(f"Заметки прочитаны из файла {filename}.")
    view = view.View()

    while True:
        view.print_titles(notes.get_titles())
        command = view.get_command()
        if command == 'q':
            logger.info("Завершение")
            break
        if command == 'n':
            logger.info("Создание")
            title = view.get_title()
            body = view.get_body()
            notes.add_note(title, body)
            continue
        if command == 'd':
            logger.info("Удаление")
            ident = view.get_ident('for delete: ')
            notes.del_note(ident)
            continue
        if command == 'r':
            logger.info("Чтение")
            ident = view.get_ident('for read')
            view.print_note(notes.read_note(ident))
            continue
        if command == 'e':
            logger.info("Редактирование")
            ident = view.get_ident('for edit')
            nt = notes.read_note(ident)
            view.print_note(nt)
            if nt == 'Not found.':
                continue
            title = view.get_title('Enter new title: ')
            body = view.get_body('Enter new text: ')
            notes.edit_note(ident, title, body)
            view.print_note(notes.read_note(ident))
            continue
        print('Wrong command')
        logger.info(f"Введена неверная команда {command}.")
