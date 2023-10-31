import re

class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tags = self.get_tags()

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"
    
    def get_tags(self):
        return set(re.findall(r'#\w+', self.text))