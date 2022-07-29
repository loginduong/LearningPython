from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel


# FirstWidget is a QWidget, and gets all the things that QWidget can do, so think of self as a QWidget
class FirstWidget(QWidget):

    # This runs when a FirstWidget is created
    def __init__(self):
        # it runs the init of the super, which I assume is QWidget? This is beyond me at the moment.
        super().__init__()

        # I need some variables! Is this proper?!
        self.labelle_string1 = "This text will change when you press that button"
        self.labelle_string2 = "OOGA BOOGA YOU JUST GOT SPOOKED"
        self.btn_changed = False

        # we then run the setup func of QWidget
        self.setup()

    # because Python runs on black magic we can define a class after needing to use it, so here is setup()
    def setup(self):
        """Sets up the GUI window and all the things in it"""
        # Quit button **********************************************************
        # btn_quit is a new object, we create it as a QPushButton with a label and self
        btn_quit = QPushButton('Quit!', self)

        # btn_quit.clicked.connect(QApplication.instance().quit()) -- This runs but doesn't close when you click it
        # btn_quit.clicked().connect(QApplication.instance().quit()) -- This does not work

        btn_quit.clicked.connect(QApplication.instance().quit)  # okay this one works, quit doesn't need parenthesis
        # Here (I assume) we "connect" the clicking action of the button to closing the instance of this QApp

        # I have no idea what this does yet
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(10, 10)

        # Let's make new buttons **********************************************
        btn_signal = QPushButton('Send Signal', self)
        btn_signal.setCheckable(True)
        btn_signal.clicked.connect(self.send_signal)
        btn_signal.move(100, 30)

        # Labels *********************************************************************
        labelle1 = QLabel("This is a Label", self)
        labelle1.move(100, 10)

        # this sets the size of the window when it appears. X pos, Y pos, width, height
        self.setGeometry(200, 100, 300, 150)
        # this I assume is setting the window's title
        self.setWindowTitle('Window Title')

        # shows the window
        self.show()

    def closeEvent(self, event: QCloseEvent):
        """Prompts the user with a message to ask if they want to close the GUI"""
        # second parameter is the question box's title, third parameter is the contents
        reply = QMessageBox.question(self, 'Message', 'Are you sure about that?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def send_signal(self):
        """Produces an 'about' message box"""
        QMessageBox.about(self, 'Title', 'Text')


# To be perfectly honest, the guide I was following proceeded to write this and not really elaborate what this did.
# The program itself will show the window as a part of the setup function so what this does is currently a mystery.
# Instantiating an instance of FirstWidget creates the GUI, but what app does is a mystery
def run():
    app = QApplication([])
    fw = FirstWidget()

    app.exec()


if __name__ == '__main__':
    run()
