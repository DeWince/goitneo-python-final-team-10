from collections import UserDict
import pickle
from Notes.note import Note


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
        if title in self.data:
            self.data[title].tags.add(tag)

    def get_note_by_title(self, title):
        return self.data.get(title, None)


    def remove_tag(self, title, tag):
        if title in self.data and tag in self.data[title].tags:
            self.data[title].tags.remove(tag)

    def find_by_tag(self, tag):
        matching_notes = []

        for title, note in self.data.items():
            if tag in note.tags:
                matching_notes.append(str(note))

        return "\n------\n".join(matching_notes)


    def sort_notes_by_tags(self):
        sorted_notes = sorted(self.data.values(), key=lambda note: sorted(note.tags)[0] if note.tags else "")
        return "\n------\n".join(str(note) for note in sorted_notes)





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

