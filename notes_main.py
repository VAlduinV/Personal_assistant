from notes_classes import *

MENU = """---Note Book Menu---
1. Add note.
2. Read note.
3. Edit note.
4. Delete note.
5. Display all notes.
6. Add tag.
7. Search.
8. Search by tags.
9. Quit"""


def input_error(function):
    def wrapper():
        try:
            result = function()
            return result
        except KeyError:
            print(f"Enter number from Note Book Menu.\n{MENU}")
        except AttributeError as e:
            print(e)
        except NoteNotFoundError as e:
            print(e)

    return wrapper


def main_note_book():
    print(MENU)

    while True:
        result = get_handler()

        if not result:
            continue

        handler = result

        if handler == "9":
            NOTES.write_data()
            break

        handler()


@input_error
def get_handler():
    action = input("Enter number of action: ")

    if action == "9":
        return action

    return COMMANDS[action]


@input_error
def add_note():
    title = Title(input("Enter title: "))
    body = Body(input("Enter note: "))
    row_tags = input("Enter tags: ")
    tags = list(map(lambda x: Tag(x), row_tags.split()))
    note = Note(title, body, tags)
    NOTES.add_note(note)


@input_error
def add_tags():
    note = NOTES.find_note(input("Enter title: "))
    note.add_tags(input("Enter tags: "))


@input_error
def delete_note():
    note = NOTES.find_note(input("Enter title: "))
    NOTES.delete_note(note)


def display_all_notes(*args):
    if NOTES:
        for note in NOTES:
            print(note)
    else:
        print("You have no notes.")


@input_error
def edit_note():
    note = NOTES.find_note(input("Enter title: "))
    new_body = Body(input("Enter note: "))
    note.edit_note(new_body)


@input_error
def read_note():
    note = NOTES.find_note(input("Enter title: "))
    note.read_note()


def search():
    substring = input("Enter substring: ")
    notes_list = []

    for note in NOTES:

        if substring in note.title.value or substring in note.body.value:
            notes_list.append(note)

    display_all_notes(notes_list)


def search_by_tag():
    tag = input("Enter tag: ")
    notes_list = []

    for note in NOTES:
        tags = list(map(lambda x: x.value, note.tags))

        if tag in tags:
            notes_list.append(note)

    display_all_notes(notes_list)


COMMANDS = {
    '1': add_note,
    '2': read_note,
    '3': edit_note,
    '4': delete_note,
    '5': display_all_notes,
    '6': add_tags,
    '7': search,
    '8': search_by_tag,
}

NOTES = NoteBook().read_data()

main_note_book()
