from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox


class UserInterface(ABC):
	@abstractmethod
	def show_commands(self):
		"""
		Метод для відображення доступних команд користувачеві.
		"""
		pass

	@abstractmethod
	def show_contacts(self, contacts):
		"""
		Метод для відображення контактів користувача.
		:param contacts: Список контактів користувача.
		"""
		pass

	@abstractmethod
	def show_notes(self, notes):
		"""
		Метод для відображення нотаток користувача.
		:param notes: Список нотаток користувача.
		"""
		pass


class ConsoleInterface(UserInterface):
	def show_commands(self):
		print("Доступні команди:")
		print("1. Відобразити контакти")
		print("2. Відобразити нотатки")
		print("3. Вийти")

	def show_contacts(self, contacts):
		print("Контакти:")
		for contact in contacts:
			print(f"{contact['name']}: {contact['phone']}")

	def show_notes(self, notes):
		print("Нотатки:")
		for note in notes:
			print(note)

	def show_no_path_found(self):
		print("Помилка: Шлях не знайдено, спробуйте знову.")

	def show_sort_files_input(self):
		print("Введіть шлях до папки, яку бажаєте відсортувати:")


# Додаткові методи реалізації консольного інтерфейсу, які взаємодіють з користувачем через командний рядок


class GUIInterface(UserInterface):
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("My App")

		# Додавання елементів графічного інтерфейсу, таких як вікна, кнопки, поля введення тощо
		self.label = tk.Label(self.root, text="Привіт, світ!")
		self.label.pack()

		self.button = tk.Button(self.root, text="Натисни мене!", command=self.button_click)
		self.button.pack()

		self.entry = tk.Entry(self.root)
		self.entry.pack()

	def show_commands(self):
		# Відображення доступних команд користувачеві на графічному інтерфейсі
		pass

	def show_contacts(self, contacts):
		# Відображення контактів користувача на графічному інтерфейсі
		pass

	def show_notes(self, notes):
		# Відображення нотаток користувача на графічному інтерфейсі
		pass

	def show_no_path_found(self):
		# Відображення помилки про незнайдений шлях на графічному інтерфейсі
		pass

	def show_sort_files_input(self):
		# Відображення елементів графічного інтерфейсу для введення шляху до папки та початку процесу сортування файлів
		pass

	def show_confirmation_dialog(self, message):
		# Відображення діалогового вікна з підтвердженням дії користувача
		result = messagebox.askyesno("Підтвердження", message)
		return result

	def show_error_dialog(self, message):
		# Відображення діалогового вікна з повідомленням про помилку
		messagebox.showerror("Помилка", message)

	def button_click(self):
		# Обробка дії користувача при натисканні кнопки
		entry_text = self.entry.get()
		self.label.config(text=f"Ви ввели: {entry_text}")

	def run(self):
		self.root.mainloop()


# Додаткові методи реалізації графічного інтерфейсу, такі як відображення вікон, кнопок,
# полів введення тощо, та обробка дій користувача через графічний інтерфейс

if __name__ == '__main__':
	gui = GUIInterface()
	gui.run()
