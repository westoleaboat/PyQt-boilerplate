# PyQt GUI application template
# qt_template.py : A blank application window

import sys                              # pass QApplication an actual list of script arguments
from PyQt5 import QtWidgets as qtw      #
from PyQt5 import QtGui as qtg          # main Qt modules.
from PyQt5 import QtCore as qtc         #


class MainWindow(qtw.QWidget):

    def __init__(self):
        """
        MainWindow constructor. Subclass of QWidget

        This widget will be our main window.
        We'll define all the UI components in here.

        Constructor ends with a call to self.show(), 
        so our MainWindow will take care of showing itself.
        """
        super().__init__()
        # Main UI code goes here

        # End main UI code
        self.show()

# Main code execution
if __name__ == '__main__':
    '''
    It's best practice to create the QApplication object at the 
    global scope (outside of any function or class). 
    This ensures that all Qt objects get properly closed 
    and cleaned up when the application quits.

    We pass sys.argv into QApplication(); Qt has several default
    command-line arguments that can be used for debugging or to alter styles and themes.
    These are processed by the QApplication constructor if you pass in sys.argv.

    We're calling app.exec() inside a call to sys.exit; this is a small touch
    that causes the exit code of app.exec() to be passed to sys.exit(), so we pass
    appropriate exit codes to the OS, if the underlying Qt instance crashes for some reason.
    '''
    # create QApplication object
    app = qtw.QApplication(sys.argv)

    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.

    # make MainWindow object
    mw = MainWindow()
    # call QApplication.exec()
    sys.exit(app.exec())