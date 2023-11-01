from collections import UserDict
import pickle
from Notes import Note


class Notes(UserDict):

    def add_note(self, title, text):
        note = Note(title, text)
        self.data[note.title] = note

    def find(self, search_str: str):
        matching_notes = []

        for title, note in self.data.items():
            if search_str in title.lower() or search_str in note.text.lower() or search_str in note.tags:
                matching_notes.append(str(note))

        return "\n------\n".join(matching_notes)

    def edit_note(self, title):
        pass


    def add_tag(self, title, tag):
        pass

    def remove_tag(self, title, tag):
        pass

    def find_by_tag(self, tag):
        pass

    def sort_notes_by_tags(self):
        pass


    def delete(self, name):
        try:
            del self.data[name]
        except KeyError:
            raise KeyError(f"Note with title '{name}' not found.")

    def save(self, filename='notebook.bin'):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, filename='notebook.bin'):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)
