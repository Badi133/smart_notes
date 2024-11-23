from note import NoteWriter
import json

notes = NoteWriter()
notes.add_note("Нотатка 1", "Мій текст", ["Hello","World"])
notes.add_note("Нотатка 2", "Мій текст 2", ["Hello"])

with open("notes.json", "w") as file:
    json.dump(notes.get_dictionary(), file)