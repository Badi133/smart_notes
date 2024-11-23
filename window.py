from ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self, notes):
        super(Window, self).__init__()

        self.notes = notes
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.notes_list.addItems(self.notes.get_dictionary().keys())

        self.ui.notes_list.currentItemChanged.connect(self.show_info)

    def show_info(self):
        selected = self.ui.notes_list.currentItem()

        note = self.notes.get_note(selected.text())
        
        self.ui.note_text.setText(note["text"])
        
        self.ui.tags_list.clear()

        for tag in note["tags"]:
            self.ui.tags_list.addItem(tag)


