from window import Window
from PyQt5.QtWidgets import QApplication
import json
from note import NoteWriter
with open("notes.json", "r") as file:
    notes = json.load(file)
    notes = NoteWriter(notes)
app = QApplication([])
window = Window(notes)
window.show()

app.exec_()

