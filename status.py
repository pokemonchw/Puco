import random
from functools import wraps
from types import FunctionType
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QLabel, QApplication
import cache, constant


def add_status(status_id:str):
    """
    添加噗可状态
    Keyword arguments:
    status_id -- 状态id
    """

    def decorator(func: FunctionType):
        @wraps(func)
        def return_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        cache.status_data[status_id] = return_wrapper

    return decorator


def handle_status(status_id:str):
    """
    处理噗可状态
    Keyword arguments:
    status_id -- 状态id
    """
    cache.status_data[status_id]()


@add_status(constant.PucoStatus.STATUS_ARDER)
def handle_status_arder():
    """ 处理噗可休闲状态 """
    if cache.puco.state_machine_id != constant.PucoStatus.STATUS_ARDER:
        cache.puco.change_movie("movie/arder.gif")
        cache.puco.state_machine_id = constant.PucoStatus.STATUS_ARDER
