import re
import random


class Note:
    note_id = 0

    def __init__(self, text):
        if len(text) == 0:
            raise ValueError("Note requires a body")

        self.number = self.note_id
        self.note_id += 1
        self.title, self.text, self.tags = self.separate_tags(text)

    def __str__(self):
        return f"#{self.number}{(' - ' + self.title) if self.title else ''}  [Tags: {', '.join(self.tags)}]\n# - {self.text}"

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
