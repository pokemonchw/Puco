import random
from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QMovie, QCursor,QMouseEvent
from PySide6.QtCore import Qt
import constant

class Puco(QWidget):

    def __init__(self):
        """ 噗可类型 """
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.repaint()
        self.img = QLabel(self)
        self.actionDatas = []
        self.state = constant.PucoStatus.STATUS_ARDER
        self.resize(128,128)
        self.state_machine_id = ""
        self.movie = QMovie("movie/StandingDraw.gif")
        self.img.setMovie(self.movie)
        self.movie.start()
        screen = QApplication.primaryScreen()
        rect = screen.availableVirtualGeometry()
        x = int((rect.width()-256)*random.random())+128
        y = int((rect.height()-256)*random.random())+128
        self.show()
        self.move(x,y)

    def mousePressEvent(self,event:QMouseEvent):
        """
        处理鼠标点击
        Keyword arguments:
        event -- 鼠标事件
        """
        if event.button() == Qt.LeftButton:
            self.m_drag = 1
            self.m_DragPostion=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self,event:QMouseEvent):
        """
        处理鼠标拖动
        Keyword arguments:
        event -- 鼠标事件
        """
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.m_DragPostion)
            event.accept()

    def change_movie(self,path:str):
        """
        更改正在播放的动画
        Keyword arguments:
        path -- 动画路径
        """
        self.movie.stop()
        self.movie.setFileName(path)
        self.img.repaint()
        self.movie.start()
