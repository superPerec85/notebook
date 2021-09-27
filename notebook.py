import os


class TextEditor:
    """Приложение блокнот, может открывать, редактировать и сохранять текстовые документы."""

    def __init__(self):
        self.action()

    def create_file(self):
        """Создает файл"""

        print('---Создание нового документа---')
        name_file = input('Имя документа: ')
        text = input('Text >>>')

        with open(f'{name_file}', 'w') as file:
            file.write(f'{text}')

        self.view_dir()

    def open_file(self):
        """Открывает файл для просмотра"""
        self.view_dir()

        name_file = input('Имя документа который нужно открыть или Q для выхода: ')

        if name_file.lower() == 'q':
            self.action()

        try:
            self.read_lines(name_file)
        except FileNotFoundError:
            print('Такого файла не существует!')

    def edit_file(self):
        """Редактирует файл (удаляет или добавляет строку)"""

        self.view_dir()

        name_file = input('Имя документа который нужно редактировать: ')

        try:
            with open(f'{name_file}', 'r') as file:
                for number, line in enumerate(file, start=1):
                    print(f'{number}. {line}')
        except FileNotFoundError:
            print('Такого файла не существует!')
            self.edit_file()

        print('\n---Выберите действие---:\na - добавить\nd - удалить строку')

        act = input('>>>').lower()

        if act == 'a':
            with open(name_file, 'a') as file:
                text = input('Text edit >>>')
                file.write(f'\n{text}')

            print(f'Файл "{name_file}" изменен')
            self.read_lines(name_file)

        elif act == 'd':
            del_string = int(input('Выберете номер строки для удаления: '))
            with open(name_file) as file:
                lines = file.readlines()

            with open(name_file, 'w') as file_edit:
                for line in lines:
                    if line != lines[del_string - 1]:
                        new_file = line
                        file_edit.write(new_file)

            print(f'Файл "{name_file}" изменен')
            self.read_lines(name_file)

        else:
            print(f'Действия "{act}" нет!')
            self.edit_file()

    def delete_file(self):
        """Удаляет файл"""
        self.view_dir()

        name_file = input('Удалить файл: ')
        try:
            os.remove(f'{name_file}')
            print(f'Файл "{name_file}" удален!')
        except FileNotFoundError:
            print('Такого файла не существует!')

    def action(self):
        """Меню действий"""

        print('\nВыберите действие:\nc - создать\no - открыть\ne - редактировать'
              '\nd - удалить\nQ - выход ')
        action_input = input('>>>').lower()

        while True:
            if action_input == 'c':
                self.create_file()
                self.action()

            elif action_input == 'o':
                self.open_file()
                self.action()

            elif action_input == 'e':
                self.edit_file()
                self.action()

            elif action_input == 'd':
                self.delete_file()
                self.action()

            elif action_input == 'q':
                print('Вы вышли из блокнота.')
                break

            else:
                print('\n*** Вы указали не доступный параметр ***')
                self.action()
            break

    def view_dir(self):
        print(os.listdir())

    def read_lines(self, name_file):
        with open(name_file, 'r') as file:
            for line in file:
                print(line)

file1 = TextEditor()
