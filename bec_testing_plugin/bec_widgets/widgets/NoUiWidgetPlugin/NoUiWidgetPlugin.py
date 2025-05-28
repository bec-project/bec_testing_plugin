from qtpy.QtWidgets import QWidget

from bec_widgets.utils.bec_widget import BECWidget



class Nouiwidgetplugin(BECWidget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
