import sys

from PySide6.QtWidgets import QApplication, QWidget

from ui_form import Ui_Calc

class Calc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Calc()
        self.ui.setupUi(self)
        self.ui.add_functions()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Calc()
    widget.show()
    sys.exit(app.exec())
