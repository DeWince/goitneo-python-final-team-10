from collections import UserDict
import pickle
from note import Note


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

    

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Note with title '{name}' has been deleted.")
        else:
            print(f"Note with title '{name}' not found.")

    def save(self, filename='notebook.bin'):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self, filename='notebook.bin'):
        with open(filename, 'rb') as file:
            self.data = pickle.load(file)



notebook = Notes()
notebook.add_note("Зустріч", "Маю зустріч завтра о 10 ранку #work")
notebook.add_note("Покупки", "Купити молоко, хліб #shop")
notebook.add_note("Робота", "Закінчити проект до п'ятниці #work")

notes_with_work_tag = notebook.find("")
print(notes_with_work_tag)