import re


class Note:
    max_note_id = None

    def __init__(self, text):
        if len(text) == 0:
            raise ValueError("Note requires a body")
        Note.max_note_id += 1
        self.number = Note.max_note_id
        self.title, self.text, self.tags = self.separate_tags(text)

    def __str__(self):
        msg = ""
        if self.title:
            msg += f" - {self.title}"
        if self.tags:
            msg += f"   Tags: {' '.join(self.tags)}"
        if len(msg):
            if len(self.text):
                msg += "\n       "
        else:
            msg = "   "
        return f"#{self.number:<3}{msg}{self.text}"

    def __repr__(self):
        return f"{self.number}|{self.title}|{self.text}|{self.tags}"

    def separate_tags(self, note_input):
        if " | " in note_input:
            title, note_input = note_input.split(" | ", 1)
        else:
            title = ""

        regex = r"#\w+"
        tags = set(re.findall(regex, note_input))
        text = re.sub(regex, "", note_input)
        return (title, text.strip().removeprefix(',').strip(), tags)
