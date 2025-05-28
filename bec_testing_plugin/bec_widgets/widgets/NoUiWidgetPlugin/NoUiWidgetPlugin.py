from bec_widgets.utils.bec_widget import BECWidget
from qtpy.QtWidgets import QWidget


class Nouiwidgetplugin(BECWidget, QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, **kwargs)
