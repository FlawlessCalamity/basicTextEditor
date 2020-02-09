from PyQt5.QtWidgets import *

bte = QApplication([])
bte.setApplicationName('Basic Text Editor')
bte.setApplicationDisplayName('jksgf')
text_area = QPlainTextEdit()
main_window = QMainWindow()
main_window.setWindowTitle('Basic Text Editor')
main_window.setCentralWidget(text_area)
menu = main_window.menuBar().addMenu('&File')
close = QAction('&Close')
close.triggered.connect(main_window.close)
menu.addAction(close)


main_window.show()
bte.exec_()
