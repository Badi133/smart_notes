class NoteWriter:
    def __init__(self, note_dict = {}):
        self.dict = note_dict

    def add_note(self, name,text, tags):
        self.dict[name] = {
            "text" : text,
            "tags": tags
        }
    def get_note(self, name):
        return self.dict[name]

    def get_dictionary(self):
        return self.dict
    


