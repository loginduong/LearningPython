from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel


# FirstWidget is a QWidget, and gets all the things that QWidget can do, so think of self as a QWidget
class FirstWidget(QWidget):

    # This runs when a FirstWidget is created
    def __init__(self):
        # it runs the init of the super
        super().__init__()
        # we then run the setup func of QWidget (what does that even do, man)
        self.setup()

    # because Python runs on black magic we can define a class after needing to use it, so here is setup()
    def setup(self):
        # Quit button **********************************************************
        # btn_quit is a new object, we create it as a QPushButton with a label and self
        btn_quit = QPushButton('BUTT', self)
        # btn_quit is set so that when you click it, the instance of QApplication closes

        # btn_quit.clicked.connect(QApplication.instance().quit()) -- This runs but doesn't close when you click it
        # btn_quit.clicked().connect(QApplication.instance().quit()) -- This does not work
        btn_quit.clicked.connect(QApplication.instance().quit)  # okay this one works, quit doesn't need parenthesis

        # I have no idea what this does yet
        btn_quit.resize(btn_quit.sizeHint())

        btn_quit.move(10, 10)

        # Let's make new buttons?? **********************************************
        btn_signal = QPushButton('Send Signal', self)
        btn_signal.setCheckable(True)
        btn_signal.clicked.connect(self.sendSignal)
        btn_signal.move(100, 30)

        # Labels *********************************************************************
        labelle1 = QLabel("This is a Label", self)
        labelle1.move(100, 10)

        # this sets the size of the window when it appears. X pos, Y pos, width, height
        self.setGeometry(200, 100, 300, 300)
        # this I assume is setting the window's title
        self.setWindowTitle('WINDOW TITLE')

        # shows the window
        self.show()

    def closeEvent(self, event: QCloseEvent):
        # second parameter is the question box's title, third parameter is the contents
        reply = QMessageBox.question(self, 'Message', 'Are you sure about that?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def sendSignal(self):
        QMessageBox.about(self, 'Title', 'Text')


def run():
    app = QApplication([])
    fw = FirstWidget()

    app.exec()


if __name__ == '__main__':
    run()
