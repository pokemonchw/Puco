import os
import sys
from PySide6.QtWidgets import QWidget, QMenu, QSystemTrayIcon
from PySide6.QtGui import QAction, QIcon
from puco import Puco

class MainMenu(QWidget):

    def __init__(self):
        """ 主ui界面类 """
        super().__init__()
        self.icon = QIcon("icon.png")
        self.quit_button = QAction("退出",self,triggered=sys.exit)
        self.quit_button.setIcon(self.icon)
        self.menu = QMenu(self)
        self.menu.addAction(self.quit_button)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()
