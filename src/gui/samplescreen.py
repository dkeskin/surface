from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from utils import Screen


class ConnectionStatus(QWidget):


    def __init__(self, _connection_status_1= "", _connection_status_2 = "", _connection_status_3 ="", _connection_status_4 = ""):


        super(ConnectionStatus, self).__init__()
        self._connection_status_1 = _connection_status_1
        self._connection_status_2 = _connection_status_2
        self._connection_status_3 = _connection_status_3
        self._connection_status_4 = _connection_status_4

        self._connection_status1_label = QLabel()
        self._connection_status2_label = QLabel()
        self._connection_status3_label = QLabel()
        self._connection_status4_label = QLabel()



        self._layout = QVBoxLayout()
        if self._connection_status_1 != "" :self._layout.addWidget(self._connection_status1_label)
        if self._connection_status_2 != "" :self._layout.addWidget(self._connection_status2_label)
        if self._connection_status_3 != "" :self._layout.addWidget(self._connection_status3_label)
        if self._connection_status_4 != "" :self._layout.addWidget(self._connection_status4_label)
        self.setLayout(self._layout)

    def _set_style(self):

        self._connection_status1_label.setAlignment(Qt.AlignCenter)
        self._connection_status2_label.setAlignment(Qt.AlignCenter)
        self._connection_status3_label.setAlignment(Qt.AlignCenter)
        self._connection_status4_label.setAlignment(Qt.AlignCenter)

        self._connection_status1_label.setText(self._connection_status_1)
        self._connection_status2_label.setText(self._connection_status_2)
        self._connection_status3_label.setText(self._connection_status_3)
        self._connection_status4_label.setText(self._connection_status_4)
        #set a different style sheet
        #pass

        self._layout.setSpacing(0)
        self.setStyleSheet("""
                    QWidget { 
                        background-color: rgb(8, 64, 67);
                    }
        """)


        self._connection_status2_label.setStyleSheet("QLabel { background-color: yellow;}")



class Raseberrypi(Screen):
    '''
    This is a screen which is going to repersent the status of the raseberry pi
    '''

    def __init__(self):
        super().__init__()
        self._connection_status = ConnectionStatus("R Pi", "Fake Status", "Arduino")


    def _config(self):
        self.resize(50,50)
        self._connection_status._set_style()
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._connection_status)
        self.setLayout(self._layout)

        self.setStyleSheet(" self { border:1px solid rgb(0, 255, 0)};")

class landStatus(Screen):
    '''
    This is a screen which is going to reperesent the status of the land status
    '''

    def __init__(self):
        super().__init__()
        self._connection_status = ConnectionStatus("LAND", "Status", "RPI")


    def _config(self):
        self.resize(50,50)
        self._connection_status._set_style()
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._connection_status)
        self.setLayout(self._layout)

        self.setStyleSheet(" self { border:1px solid rgb(0, 255, 0)};")



if __name__ == "__main__":
    app = QApplication()
    form = Raseberrypi()
    form._config()
    form.show()
    app.exec_()
