from src.utils import clean_text

class Document:
    def __init__(self,title,text):
        self.title = title
        self.text = text

    def cleaned(self):
        return clean_text(self.text)