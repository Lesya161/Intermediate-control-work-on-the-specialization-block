import notes


class View:

    def print_titles(self, titles):
        print('\nId Title')
        for x in titles:
            print(f'{x[0]}: {x[1]}')

    def get_command(self):
        return input('Enter command (n - new, d - delete, e - edit, r - read, q - quit): ')

    def get_title(self, text='Enter title: '):
        return input(text)

    def get_body(self, text='Enter text: '):
        return input(text)

    def get_ident(self, text=''):
        return input(f'Enter id {text}: ')

    def print_note(self, note):
        print(note)