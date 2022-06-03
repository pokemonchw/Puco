#!/usr/bin/python3
import sys
from PySide6.QtWidgets import QApplication
from ui import menu
import cache, status,ai,constant
from puco import Puco


def change_status(status_id:str):
    """
    更改噗可状态
    Keyword arguments:
    status_id -- 状态id
    """
    cache.status_data[constant.PucoStatus.STATUS_ARDER]()

app = QApplication(sys.argv)
main_menu = menu.MainMenu()
cache.puco = Puco()
ai_thread = ai.AIThread()
ai_thread.status_signal.connect(change_status)
ai_thread.start()
app.exec()
