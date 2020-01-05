from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from utils import Screen


class ConnectionStatus(QWidget):

    def __init__(self, _connection_status_header="", _connection_status_body = [],
                 _connection_status_footer=""):
        """

        :param _connection_status_header: The header of the status
        :param _connection_status_body: Holds an array of status
        :param _connection_status_footer: the footer for the status
        """
        super(ConnectionStatus, self).__init__()
        self._connection_status_header = _connection_status_header
        self._connection_status_body = _connection_status_body
        self._connection_status_footer = _connection_status_footer

        self._layout = QVBoxLayout()  # create a QVboxLayout for the frame
        self._layout_l = QGridLayout()  # create a QVboxLayout for the frame
        self._connection_status_header_label = QLabel()  # create a label for the frame
        self._connection_status_footer_label = QLabel()

        self._layout.addWidget(self._connection_status_header_label)
        self._status_dict = {}  # A status dictionary to store all the status of the dictionary

        # makes a directory to connect a label to connection status.
        self._frame = QFrame();
        for x in self._connection_status_body:
            label = QLabel()
            self._status_dict[label] = x
            self._layout_l.addWidget(label)

        self._frame.setLayout(self._layout_l)

        self._layout.addWidget(self._frame)
        self._layout.addWidget(self._connection_status_footer_label)

        self.setLayout(self._layout)  # then set the layout widget
        self._set_style()

    def _set_style(self):

        self._layout.setSpacing(0);

        for key, value in {self._connection_status_header_label: self._connection_status_header,
                           self._connection_status_footer_label: self._connection_status_footer}.items():
            key.setAlignment(Qt.AlignCenter)
            key.setText(value)

        for key, value in self._status_dict.items():
            key.setAlignment(Qt.AlignCenter)
            key.setText(value)
            key.setStyleSheet("""
                font-size: 20px;
                background-color: orange;
                            """)

        self._frame.setStyleSheet("""background-color: orange;
                                              border: none;""")
        self.setStyleSheet("""
            QWidget {   
               font-family: Arial;
               background-color: rgb(8, 64, 67);
            }
            
            QFrame {
              border: 5px solid orange;
            }
            
            QLabel {
               color: white;
                font-family: cursive
            }
            """)

        def update_values(self):
            pass


class ConnectionStatusSample(Screen):
    """
    This is a screen which is going to represent the status of the raspberry pi
    """

    def __init__(self):
        super().__init__()
        self._raspberry_pi = ConnectionStatus("R Pi", ["Fake Status"], "Arduino")
        self._land = ConnectionStatus("LAND", ["Fake Status"], "R Pi")

    def _config(self):
        self._layout = QHBoxLayout()
        self._layout.addWidget(self._raspberry_pi)
        self._layout.addWidget(self._land)
        self.setLayout(self._layout)


if __name__ == "__main__":
    app = QApplication()
    form = ConnectionStatusSample()
    form._config()
    form.show()
    app.exec_()
