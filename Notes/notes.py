from collections import UserDict
from Notes.note import Note


class Notes(UserDict):

    def find(self, search_str: str):
        matching_notes = []

        for note in self.data.values():
            if search_str.casefold() in repr(note).casefold():
                matching_notes.append(str(note))

        return self.print_notes(matching_notes)

    def get_note_by_id(self, idx):
        idx = int(idx)
        note = self.data.get(idx, None)
        if not note:
            raise KeyError(f"Note with number '{idx}' not found")
        return note

    def add_note(self, text):
        if not Note.max_note_id:
            Note.max_note_id = max([note.number for note in self.values()])
        note = Note(text)
        self.data[note.number] = note

    def edit_note(self, idx, new_text):
        idx = int(idx)
        note = self.get_note_by_id(idx)
        note.title, note.text, note.tags = note.separate_tags(new_text)

    def delete(self, idx):
        idx = int(idx)
        self.get_note_by_id(idx)
        del self.data[idx]

    def add_tag(self, idx, tag):
        idx = int(idx)
        if idx in self.data:
            self.data[idx].tags.add(tag)

    def remove_tag(self, idx, tag):
        idx = int(idx)
        if idx in self.data and tag in self.data[idx].tags:
            self.data[idx].tags.remove(tag)

    def find_by_tag(self, tag):
        matching_notes = []

        for note in self.data.values():
            if tag in note.tags:
                matching_notes.append(str(note))

        return self.print_notes(matching_notes)

    def sort_notes_by_tags(self):
        sorted_notes = sorted(self.data.values(), key=lambda note: sorted(note.tags)[0] if note.tags else "")
        return self.print_notes(sorted_notes)

    def print_notes(self, notes):
        return "\n------\n".join(map(str, notes)) + "\n"
