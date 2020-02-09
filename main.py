from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

file_path = None


class MainWindow(QMainWindow):
    def closeEvent(self, e)


################# application ###################
#################################################
bte = QApplication([])
bte.setApplicationName('Basic Text Editor')
bte.setApplicationDisplayName('jksgf')
################# application ###################


################# main window widget ###################
########################################################
text_area = QPlainTextEdit()
main_window = QMainWindow()
main_window.setWindowTitle('Basic Text Editor')
main_window.setCentralWidget(text_area)
################# main window widget ###################


################# menus ###################
############################################
help_menu = main_window.menuBar().addMenu('&Help')
menu = main_window.menuBar().addMenu('&File')

open_file = QAction('&Open')
save_action = QAction('&Save')
save_as = QAction('Save &As...')
close = QAction('&Close')
about_action = QAction('&About')

open_file.setShortcut(QKeySequence.Open)
save_action.setShortcut(QKeySequence.Save)

menu.addAction(open_file)
menu.addAction(save_action)
menu.addAction(save_as)
menu.addAction(close)
help_menu.addAction(about_action)


################# menus ###################


def open_file_dialog():
    global file_path
    path = QFileDialog.getOpenFileName(main_window, 'Open')[0]
    if path:
        text_area.setPlainText(open(path).read())
        file_path = path


def save_dialog():
    if file_path is None:
        save_as_dialog()
    else:
        with open(file_path, 'w') as f:
            f.write(text_area.toPlainText())


def save_as_dialog():
    global file_path
    path = QFileDialog.getSaveFileName(main_window, 'Save As')[0]
    if path:
        file_path = path
        save_action()


def show_about_dialog():
    text = '<center>'\
        '<h1>Basic Text Editor</h1>'\
        '</center>'\
        '<p>Version: 1.0</p>'
    QMessageBox.about(main_window, 'About the Basic Text Editor', text)


close.triggered.connect(main_window.close)
save_action.triggered.connect(save_dialog)
save_as.triggered.connect(save_as_dialog)
about_action.triggered.connect(show_about_dialog)
open_file.triggered.connect(open_file_dialog)
main_window.show()
bte.exec_()
