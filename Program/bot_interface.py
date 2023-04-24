import os
import tkinter as tk
from file_sorter import FileSorter
import subprocess

# Імпортуємо класи UserInterface та ConsoleInterface з вихідного коду
from abc import ABC, abstractmethod

current_process = None


class BotInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x1000")
        self.root.title("B0tHe1Per")
        self.root.config(bg="black")

        # Создаем метки для надписей "B0t", "Hel" и "Per"
        self.label_bot = tk.Label(
            self.root, text="B0t", font=("Lucida Handwriting", 60), fg="red", bg="black"
        )
        self.label_hel = tk.Label(
            self.root,
            text="He1",
            font=("Lucida Handwriting", 60),
            fg="green",
            bg="black",
        )
        self.label_per = tk.Label(
            self.root,
            text="Per",
            font=("Lucida Handwriting", 60),
            fg="blue",
            bg="black",
        )

        # Устанавливаем метки в верхнюю часть окна
        self.label_bot.place(x=230, y=70, anchor="center")
        self.label_hel.place(x=400, y=70, anchor="center")
        self.label_per.place(x=560, y=70, anchor="center")

        # Создаем кнопки
        self.button_sort = tk.Button(
            self.root,
            text="Sort Files",
            font=("Lucida Handwriting", 30),
            bg="black",
            fg="white",
            command=self.sort_files,
        )
        self.button_address = tk.Button(
            self.root,
            text="Address Book",
            font=("Lucida Handwriting", 30),
            bg="black",
            fg="white",
            command=self.address_book,
        )
        self.button_notes = tk.Button(
            self.root,
            text="Notes",
            font=("Lucida Handwriting", 30),
            bg="black",
            fg="white",
            command=self.notes,
        )
        self.button_exit = tk.Button(
            self.root,
            text="Exit",
            font=("Lucida Handwriting", 30),
            bg="black",
            fg="white",
            command=self.exit,
        )

        # Устанавливаем кнопки на экран
        self.button_sort.place(x=400, y=250, anchor="center")
        self.button_address.place(x=400, y=370, anchor="center")
        self.button_notes.place(x=400, y=490, anchor="center")
        self.button_exit.place(x=400, y=610, anchor="center")

        self.input_folder_address = None
        self.label_input_folder_address = None
        self.button_return = None
        self.button_sort_files = None
        self.label_no_path_found = None

    def show_no_path_found(self):
        # Ця функція створює мітку, яка вказує, що шлях не знайдено, і відображає її на екрані.
        if not self.label_no_path_found:
            self.label_no_path_found = tk.Label(
                self.root,
                text="No path found, try again.",
                font=("Arial", 20),
                fg="red",
                bg="black",
            )
        self.label_no_path_found.config(text="No path found, try again.")
        self.button_sort_files.config(text="No path found, try again.", fg="red")
        self.root.after(1000, self.hide_input_error)

    def hide_input_error(self):
        # Ця функція приховує мітку, яка вказує, що шлях не знайдено.
        if hasattr(self, "label_no_path_found"):
            self.label_no_path_found.destroy()

    def show_sort_files_input(self):
        # Ця функція показує елементи GUI, необхідні користувачеві для введення шляху до папки
        # та початку процесу сортування файлів.
        self.button_sort.place_forget()
        self.button_address.place_forget()
        self.button_notes.place_forget()
        self.button_exit.place_forget()

        self.input_folder_address = tk.Entry(self.root, font=("Arial", 20), width=45)
        self.input_folder_address.place(x=50, y=400)

        self.label_input_folder_address = tk.Label(
            self.root,
            text="Input folder path:",
            font=("Arial", 20),
            fg="white",
            bg="black",
        )
        self.label_input_folder_address.place(x=50, y=350)

        self.button_sort_files = tk.Button(
            self.root,
            text="Press to sort",
            font=("Arial", 20),
            bg="black",
            fg="white",
            width=10,
            command=self.sort_files_by_button,
        )
        self.button_sort_files.place(x=400, y=500, anchor="center")

        self.button_return = tk.Button(
            self.root,
            text="Return to menu",
            font=("Arial", 20),
            bg="black",
            fg="white",
            command=self.return_to_menu,
        )
        self.button_return.place(x=400, y=750, anchor="center")

    def sort_files_by_button(self):
        # Ця функція отримує шлях до папки з введених користувачем даних, перевіряє,
        # чи це дійсний каталог, сортує файли в папці та повертає до головного меню.
        folder_address = self.input_folder_address.get()
        if os.path.isdir(folder_address):
            sorter = FileSorter(folder_address)
            sorter.normalize(folder_address)
            sorter.sort_files()
            sorter.sort_archives()
            print(f"{folder_address} files sorted")
            self.return_to_menu()
        else:
            self.label_input_folder_address.config(
                text="No path found, try again.", fg="red"
            )
            self.root.after(1000, self.input_folder_address.delete, 0, tk.END)
            if self.label_no_path_found:
                self.label_no_path_found.place(x=400, y=550, anchor="center")
                self.root.after(1000, self.label_no_path_found.place_forget)
            self.button_sort_files.config(text="Press to sort", fg="white")

    def return_to_menu(self):
        # Ця функція приховує елементи GUI для сортування файлів і повертає до головного меню.
        self.input_folder_address.destroy()
        self.label_input_folder_address.destroy()
        self.button_return.destroy()
        self.button_sort_files.destroy()

        self.button_sort.place(x=400, y=200, anchor="center")
        self.button_address.place(x=400, y=300, anchor="center")
        self.button_notes.place(x=400, y=400, anchor="center")
        self.button_exit.place(x=400, y=500, anchor="center")

    def sort_files(self):
        # Відображати поля введення та кнопки для сортування файлів
        self.show_sort_files_input()

    def close_current_process(self):
        # Закрийте поточний процес, якщо він запущений
        global current_process
        if current_process is not None:
            current_process.kill()

    def address_book(self):
        # Запустіть програму адресної книги та закрийте всі наявні процеси
        global current_process
        self.close_current_process()
        current_process = subprocess.Popen(["python", "address_book.py"])

    def notes(self):
        # Запустіть програму нотаток і закрийте будь-який існуючий процес
        global current_process
        self.close_current_process()
        current_process = subprocess.Popen(["python", "notes_main.py"])

    def on_closing(self):
        # Закрийте поточний процес, якщо він запущений, і знищіть кореневе вікно
        global current_process
        if current_process is not None:
            current_process.kill()
        self.root.destroy()

    def exit(self):
        # Закрити поточний процес і знищити кореневе вікно
        self.close_current_process()
        self.root.destroy()

    def run(self):
        # Запустити головний цикл подій кореневого вікна
        self.root.mainloop()


class UserInterface(ABC):
    @abstractmethod
    def show_cards(self, cards):
        pass

    @abstractmethod
    def show_notes(self, notes):
        pass

    @abstractmethod
    def show_available_commands(self, commands):
        pass


class ConsoleInterface(UserInterface):
    def show_cards(self, cards):
        # Виводимо картки з контактами користувача в консоль
        print("Contacts:")
        for card in cards:
            print(
                f"Name: {card['name']}, Phone: {card['phone']}, Email: {card['email']}"
            )

    def show_notes(self, notes):
        # Виводимо нотатки користувача в консоль
        print("Notes:")
        for note in notes:
            print(note)

    def show_available_commands(self, commands):
        # Виводимо доступні команди в консоль
        print("Available commands:")
        for command in commands:
            print(command)


if __name__ == "__main__":
    print(
        """
▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌  ▐░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌  ▄█░░░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▐░░▌▐░░▌    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌▐░▌    ▐░▌    ▐░▌     ▐░▌       ▐░▌▐░▌            ▀▀ ▐░░▌    ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌    ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░░▌    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░▌  ▐░▌  ▐░▌    ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌    ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░░▌    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌    ▐░▌▐░▌    ▐░▌     ▐░▌       ▐░▌▐░▌               ▐░░▌    ▐░▌          ▐░▌          ▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄█░█░▌    ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄█░░█▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░▌  ▐░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                                    
        """
    )
    bot = BotInterface()
    bot.run()
    # Тестуємо клас ConsoleInterface
    # Створення об'єкту класу ConsoleInterface
    console_interface = ConsoleInterface()

    # Заготовка даних для тестування
    test_cards = [
        {"name": "John", "phone": "123456789", "email": "john@example.com"},
        {"name": "Jane", "phone": "987654321", "email": "jane@example.com"},
    ]
    test_notes = ["Note 1", "Note 2", "Note 3"]
    test_commands = ["Command 1", "Command 2", "Command 3"]

    # Виклик методів класу ConsoleInterface для виводу даних в консоль
    console_interface.show_cards(test_cards)
    console_interface.show_notes(test_notes)
    console_interface.show_available_commands(test_commands)
