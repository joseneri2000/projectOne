import sys
from PyQt6.QtWidgets import QApplication
from gui import VoteGUI
from logic import VoteLogic

def main():
    app = QApplication(sys.argv)
    logic = VoteLogic()
    gui = VoteGUI(logic)
    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
