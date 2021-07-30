from PyQt5.QtWidgets  import *
import sys
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.showMaximized()



app = QApplication(sys.argv)
QApplication.setApplicationName("MY BROWSER")
window = MainWindow()
app.exec_()