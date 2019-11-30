import typing
import random
from .utils import Screen
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

_LOW_LEAK = 20
_LOW_TEMPERATURE = 30
_LOW_DEPTH = 300
_LOW_ACCELERATION = 5
_CRITICAL_LEAK = 50
_CRITICAL_TEMPERATURE = 50
_CRITICAL_DEPTH = 500
_CRITICAL_ACCELERATION = 10

_CLOCK_INTERVAL = 1000


class Indicator(QWidget):

    def __init__(self, header: str, body: str, *, low_limit: float = None, high_limit: float = None,
                 text_format_func: typing.Callable = None):
        """
        TODO: Document

        .. warning::

            `text_format_func` must follow the signature present in `_default_text_format`.

        :param header: Header text displayed above the values
        :param body: Body containing the values
        :param low_limit: Optional, lower limit of the values
        :param high_limit: Optional, higher limit of the values
        :param text_format_func: Optional text formatting function for custom text rendering
        """
        super(Indicator, self).__init__()
        self._low_limit = low_limit
        self._high_limit = high_limit
        self._header = header
        self._body = body

        # Remember the number of "{}" elements which will be formatted via Python string formatting
        self._placeholder_count = self._body.count("{}")

        # The text formatting function should be flexible for each indicator, so allow passing a specific one
        self._text_format_func = text_format_func if text_format_func else self._default_text_format

        # Create the QT objects and set the layout
        self._layout = QVBoxLayout()
        self._header_label = QLabel()
        self._body_label = QLabel()
        self._footer_label = QLabel()
        self._layout.addWidget(self._header_label)
        self._layout.addWidget(self._body_label)
        self._layout.addWidget(self._footer_label)
        self.setLayout(self._layout)

        # Set the style and initially update the visible items
        self._set_style()
        self._header_label.setText(self._header)
        self.update_text(*("0" for _ in range(self._placeholder_count)))

    @staticmethod
    def _default_text_format(body: str, body_label: QLabel, *args):
        """
        TODO: Document

        By default renders everything except for units with font-size 60, whereas the units have font-size set to 30.

        :param body: Body text containing the values to format
        :param body_label: QLabel wrapper around the body
        :param args: New values to be displayed
        """
        index = body.rfind("{}") + 2
        text = body[:index] + "<span style=\"font-size:30px;\">" + body[index:] + "</span>"
        text = text.replace("\n", "<br>")
        text = text.format(*args)
        body_label.setText(text)

    def _set_style(self):
        """
        TODO: Document
        """
        self._body_label.setAlignment(Qt.AlignCenter)
        self._header_label.setAlignment(Qt.AlignHCenter)
        self._layout.setSpacing(0)

        # Each element has its own style sheet for maximum flexibility
        self.setStyleSheet("""
            QWidget { 
                background-color: rgb(8, 64, 67);
            }
            """)
        self._header_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 30px;
            }
        """)
        self._footer_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 30px;
            }
        """)
        self._body_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 60px;
            }
        """)

        # Maximum size here is just for the sample screen
        self.setMaximumSize(300, 300)

        # Make sure the body takes as much of the space as possible by making the header and footer as small as possible
        self._header_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self._footer_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Rich text flag is mandatory due to the HTML code injections within the label's text
        self._body_label.setTextFormat(Qt.RichText)

    def update_text(self, *args):
        """
        TODO: Document

        :param args: New values to display
        """

        if len(args) != self._placeholder_count:
            raise ValueError(f"Mismatch between expected number of arguments: {len(self._format_chars_count)}, "
                             f"and received: {len(args)}")
        if len(args) > 0:
            self._text_format_func(self._body, self._body_label, *args)
        else:
            self._body_label.setText(self._body)

        if len(args) == 1 and self._low_limit is not None and self._high_limit is not None:
            value = args[0]

            # Initial value is empty string
            if isinstance(value, str) and value.isdigit():
                value = int(value)

            if value < self._low_limit:
                self._body_label.setStyleSheet("""
                    QLabel {
                        color: blue;
                        font-size: 60px;
                    }
                """)
            elif value > self._high_limit:
                self._body_label.setStyleSheet("""
                    QLabel {
                        color: red;
                        font-size: 60px;
                    }
                """)
            else:
                self._body_label.setStyleSheet("""
                    QLabel {
                        color: white;
                        font-size: 60px;
                    }
                """)


class IndicatorSample(Screen):
    """
    TODO: Document

    Should be a widget inside the actual screen.
    """

    def __init__(self):
        """
        TODO: Document
        """
        super(IndicatorSample, self).__init__()

        self._layout = QHBoxLayout()
        self._leak = Indicator("Leak", "{}%", low_limit=_LOW_LEAK, high_limit=_CRITICAL_LEAK)
        self._temp = Indicator("Temperature", "{}℃", low_limit=_LOW_TEMPERATURE, high_limit=_CRITICAL_TEMPERATURE)
        self._depth = Indicator("Depth", "{}cm", low_limit=_LOW_DEPTH, high_limit=_CRITICAL_DEPTH)
        self._acc = Indicator("Acceleration", "{}m/s", low_limit=_LOW_ACCELERATION, high_limit=_CRITICAL_ACCELERATION)
        self._rot = Indicator("Rotation:", "x: {}\ny: {}\nz: {}")

        self._config()
        self.setLayout(self._layout)

        self._clock = QTimer()
        self._clock.setInterval(_CLOCK_INTERVAL)
        self._clock.timeout.connect(self._sample_update)

    def update_leak(self):
        """
        TODO: Document

        Placeholder, uses fake data
        """
        fake = random.randint(0, 100)
        self._leak.update_text(fake)

    def update_temperature(self):
        """
        TODO: Document

        Placeholder, uses fake data
        """
        fake = random.randint(0, 100)
        self._temp.update_text(fake)

    def update_depth(self):
        """
        TODO: Document

        Placeholder, uses fake data
        """
        fake = random.randint(0, 100)
        self._depth.update_text(fake)

    def update_acceleration(self):
        """
        TODO: Document

        Placeholder, uses fake data
        """
        fake = random.randint(0, 100)
        self._acc.update_text(fake)

    def update_rotation(self):
        """
        TODO: Document

        Placeholder, uses fake data
        """
        fake, fake2, fake3 = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
        self._rot.update_text(fake, fake2, fake3)

    def _sample_update(self):
        self.update_acceleration()
        self.update_depth()
        self.update_rotation()
        self.update_leak()
        self.update_temperature()

    def _config(self):
        """
        TODO: Document
        """
        self._layout.addWidget(self._leak)
        self._layout.addWidget(self._temp)
        self._layout.addWidget(self._depth)
        self._layout.addWidget(self._acc)
        self._layout.addWidget(self._rot)

    def _set_style(self):
        """
        TODO: Document
        """
        super()._set_style()

    def post_init(self):
        """
        TODO: Document
        """
        super().post_init()

    def on_switch(self):
        """
        TODO: Document
        """
        super().on_switch()
        self._clock.start()
